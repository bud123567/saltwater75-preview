/* Refresh the lineup baked into saltwater75-entertainment.html.
 *
 * Boom Calendar has no public API — it ships the events inside its widget —
 * so the only reliable read is to let the Wix page render and walk the
 * calendar's own DOM, stepping months with its "next" arrow.
 *
 *   node tools/sync-events.js [months]
 *
 * Rewrites the <script id="ent-events"> block in place. Exits non-zero
 * without touching the file if it can't reach the calendar, so a failed run
 * never blanks the page.
 */
const fs = require('fs');
const path = require('path');

const PAGE = 'https://www.saltwater75.com/entertainment-calendar';
const TARGET = path.join(__dirname, '..', 'saltwater75-entertainment.html');
const MONTHS = +(process.argv[2] || 10);

/* CI installs full puppeteer (bundled Chromium); locally puppeteer-core drives
   the Chrome that's already on the machine. */
let puppeteer, launchOpts = { headless: 'new', args: ['--no-sandbox', '--disable-gpu'] };
try {
  puppeteer = require('puppeteer');
} catch (e) {
  puppeteer = require('puppeteer-core');
  launchOpts.executablePath = process.env.CHROME_PATH ||
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
}

const readMonth = () => {
  const out = [];
  document.querySelectorAll('[data-date]').forEach(cell => {
    const date = cell.getAttribute('data-date');
    if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) return;
    cell.querySelectorAll('.fc-event, .fc-daygrid-event, a[class*="event"]').forEach(ev => {
      const el = ev.querySelector('.fc-event-title, .fc-sticky, .fc-event-title-container') || ev;
      const title = el.innerText.trim().replace(/\s+/g, ' ');
      if (title) out.push({ date, title });
    });
  });
  return out;
};

(async () => {
  const browser = await puppeteer.launch(launchOpts);
  const page = await browser.newPage();
  await page.setViewport({ width: 1000, height: 1300 });
  await page.goto(PAGE, { waitUntil: 'networkidle2', timeout: 90000 });
  await new Promise(r => setTimeout(r, 15000));

  const frame = page.frames().find(f => /calendar\.boomte\.ch\/widget/.test(f.url()));
  if (!frame) throw new Error('calendar widget never loaded');

  const seen = new Set(), events = [];
  for (let i = 0; i < MONTHS; i++) {
    (await frame.evaluate(readMonth)).forEach(r => {
      const k = r.date + '|' + r.title;
      if (!seen.has(k)) { seen.add(k); events.push(r); }
    });
    const next = await frame.$('.fc-next-button, button[title*="Next"], [class*="next"]');
    if (!next) break;
    await next.click().catch(() => {});
    await new Promise(r => setTimeout(r, 2500));
  }
  await browser.close();

  if (!events.length) throw new Error('calendar rendered but no events found');
  events.sort((a, b) => a.date.localeCompare(b.date) || a.title.localeCompare(b.title));

  const block = '      [\n' +
    events.map(e => '      ' + JSON.stringify(e)).join(',\n') + '\n      ]';
  const html = fs.readFileSync(TARGET, 'utf8');
  const next = html.replace(
    /(<script type="application\/json" id="ent-events">\n)[\s\S]*?(\n\s*<\/script>)/,
    (_, open, close) => open + block + close);

  if (next === html) { console.log(`${events.length} events — no change`); return; }
  fs.writeFileSync(TARGET, next);
  console.log(`${events.length} events written to ${path.basename(TARGET)}`);
})().catch(e => { console.error('sync failed:', e.message); process.exit(1); });
