/* Refresh the lineup baked into saltwater75-entertainment.html.
 *
 * Boom Calendar has no public API — it ships the events inside its widget — so
 * the only reliable read is to let the Wix page render and walk the calendar's
 * own DOM. It takes two passes, because neither view has everything:
 *
 *   month grid (desktop layout)  every date, no set times
 *   agenda     (mobile layout)   set times, upcoming events only
 *
 * Dates come from the grid; times are matched onto them from the agenda.
 *
 *   node tools/sync-events.js [months]
 *
 * Rewrites the <script id="ent-events"> block in place. Exits non-zero without
 * touching the file if it can't reach the calendar, so a failed run never
 * blanks the page.
 */
const fs = require('fs');
const path = require('path');

const PAGE = 'https://www.saltwater75.com/entertainment-calendar';
const TARGET = path.join(__dirname, '..', 'saltwater75-entertainment.html');
const MONTHS = +(process.argv[2] || 10);

const DESKTOP_UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ' +
                   '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const MOBILE_UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 ' +
                  '(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1';

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

const wait = ms => new Promise(r => setTimeout(r, ms));

/* Open the page under a given user-agent — which is what decides whether Wix
   serves the desktop or mobile layout — and hand back the widget's frame. */
async function openWidget(browser, ua, width) {
  const page = await browser.newPage();
  await page.setViewport({ width, height: 1400 });
  await page.setUserAgent(ua);
  await page.goto(PAGE, { waitUntil: 'networkidle2', timeout: 90000 });
  await wait(16000);
  const frame = page.frames().find(f => /calendar\.boomte\.ch\/widget/.test(f.url()));
  if (!frame) throw new Error('calendar widget never loaded');
  return { page, frame };
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

/* Dates and act names, stepping months with the widget's own next arrow. */
async function collectDates(browser) {
  const { page, frame } = await openWidget(browser, DESKTOP_UA, 1000);
  const seen = new Set(), events = [];
  for (let i = 0; i < MONTHS; i++) {
    (await frame.evaluate(readMonth)).forEach(r => {
      const k = r.date + '|' + r.title;
      if (!seen.has(k)) { seen.add(k); events.push(r); }
    });
    const next = await frame.$('.fc-next-button, button[title*="Next"], [class*="next"]');
    if (!next) break;
    await next.click().catch(() => {});
    await wait(2500);
  }
  await page.close();
  return events;
}

/* Set times, from the agenda view. Reached through the ☰ on the mobile layout,
   where the view menu lives; the list pages in as it is scrolled. */
async function collectTimes(browser) {
  const { page, frame } = await openWidget(browser, MOBILE_UA, 320);

  await frame.evaluate(() => {
    const el = [...document.querySelectorAll('button,[role="button"],[class*="menu"]')]
      .find(e => /sideMenu|menu|burger/i.test((e.className || '').toString()));
    if (el) el.click();
  });
  await wait(2500);
  await frame.evaluate(() => {
    const el = [...document.querySelectorAll('*')]
      .find(e => e.children.length === 0 && /^agenda$/i.test((e.innerText || '').trim()));
    if (el) el.click();
  });
  await wait(5000);

  let last = -1;
  for (let i = 0; i < 40; i++) {
    const n = await frame.evaluate(() => {
      const sc = document.querySelector('.load-more-on-scroll');
      if (sc) sc.scrollTop = sc.scrollHeight;
      return document.querySelectorAll('.agenda-item').length;
    });
    if (n === last) break;
    last = n;
    await wait(1200);
  }

  const rows = await frame.evaluate(() =>
    [...document.querySelectorAll('.agenda-item')].map(it => {
      const t = it.querySelector('.agenda-item-title');
      return { title: t ? t.innerText.trim() : '',
               raw: it.innerText.trim().replace(/\s*\n\s*/g, '|') };
    }));
  await page.close();

  const MON = { January: 1, February: 2, March: 3, April: 4, May: 5, June: 6, July: 7,
                August: 8, September: 9, October: 10, November: 11, December: 12 };
  const times = {};
  rows.forEach(a => {
    const p = a.raw.split('|');                  // day|Month|Weekday|Title|4:00 pm - 8:00 pm|…
    const day = +p[0], mon = MON[p[1]], t = (p[4] || '').trim();
    if (mon && day && a.title && /\d/.test(t)) {
      times[mon + '-' + day + '|' + a.title] = t.replace(/\s*-\s*/, ' – ').replace(/\s+/g, ' ');
    }
  });
  return times;
}

(async () => {
  const browser = await puppeteer.launch(launchOpts);
  let events, times = {};
  try {
    events = await collectDates(browser);
    /* Times are a bonus — a page with dates and no times still beats no page. */
    try { times = await collectTimes(browser); }
    catch (e) { console.error('agenda pass skipped:', e.message); }
  } finally {
    await browser.close();
  }

  if (!events.length) throw new Error('calendar rendered but no events found');

  events.forEach(e => {
    const [, m, d] = e.date.split('-').map(Number);
    const t = times[m + '-' + d + '|' + e.title];
    if (t) e.time = t;
  });
  events.sort((a, b) => a.date.localeCompare(b.date) || a.title.localeCompare(b.title));
  console.log(`${events.length} events, ${events.filter(e => e.time).length} with set times`);

  const block = '      [\n' +
    events.map(e => '      ' + JSON.stringify(e)).join(',\n') + '\n      ]';
  const html = fs.readFileSync(TARGET, 'utf8');
  const next = html.replace(
    /(<script type="application\/json" id="ent-events">\n)[\s\S]*?(\n\s*<\/script>)/,
    (_, open, close) => open + block + close);

  if (next === html) { console.log('no change'); return; }
  fs.writeFileSync(TARGET, next);
  console.log(`written to ${path.basename(TARGET)}`);
})().catch(e => { console.error('sync failed:', e.message); process.exit(1); });
