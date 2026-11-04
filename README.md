# NJ History Daily — TelVue RSS starter

This project creates a small RSS 2.0 feed for a TelVue HyperCaster ticker.

## What it does

- Reads `history.json`.
- Uses the current date in the `America/New_York` time zone.
- Publishes the matching date's New Jersey history item to `feed.xml`.
- Runs every day through GitHub Actions and commits the updated feed.
- If that date has not yet been researched and added, it publishes a transparent placeholder rather than inventing a historical event.

## Important: starter content

The included `history.json` contains a small set of sourced example dates, not a complete 366-day calendar. Add and verify entries before relying on it every day on air. Each entry needs:
- `date`: month and day as `MM-DD`
- `year`: year of the historical event
- `title`: short headline
- `text`: concise ticker-friendly description
- `source`: source name
- `source_url`: direct source URL

Keep the wording short enough for your ticker. Verify dates and details against the linked source.

## Publish with GitHub Pages

1. Create a **public** GitHub repository named `nj-history-daily`.
2. Upload all files and folders from this project to the repository's `main` branch. Make sure `.github/workflows/update-feed.yml` is included.
3. Open **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Choose branch **main** and folder **/(root)**, then Save.
6. Open **Actions** and enable workflows if GitHub asks.
7. Open the workflow named **Update New Jersey history RSS** and choose **Run workflow** once.
8. After GitHub Pages finishes publishing, your feed URL will be:

   `https://YOUR-USERNAME.github.io/nj-history-daily/feed.xml`

Replace `YOUR-USERNAME` with your GitHub username.

## Before connecting TelVue

Open the feed URL in a browser. It should show XML beginning with `<?xml ...` and an `<rss version="2.0">` element. Then paste that exact URL into the RSS feed configuration in HyperCaster and preview/test the ticker.

## Daily automation

The scheduled workflow runs at 10:15 UTC (5:15 a.m. Eastern Standard Time or 6:15 a.m. Eastern Daylight Time). GitHub Actions schedules can be delayed occasionally. You can also run it manually from the Actions tab.

## Sources used for the starter entries

- New Jersey State Archives: https://www.nj.gov/state/archives/documentary-treasures.shtml
- New Jersey State Archives, Constitution ratification minutes: https://www.nj.gov/state/archives/documentary-treasures-us-constitution-convention-minutes.shtml
- National Park Service American Revolution timeline: https://www.nps.gov/subjects/americanrevolution/timeline.htm
- Garden State Parkway history: https://gsphistory.njta.gov/
- New Jersey historical chronology: https://www.getnj.com/njags/chronology/chronologyto1800.shtml

## Notes

- GitHub Pages sites are public. This feed contains public historical information only.
- The workflow writes only `feed.xml`; edit `history.json` to add or correct historical entries.
- GitHub Pages is static hosting. GitHub Actions generates and commits the XML file; Pages then serves it.
- <!-- deployment refresh -->
