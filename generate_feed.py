#!/usr/bin/env python3
"""Build a date-specific RSS 2.0 feed for This Day in New Jersey History."""
import json
import os
from datetime import datetime
from email.utils import format_datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
SITE_URL = os.environ.get(
    "SITE_URL",
    "https://woodbridgetv.github.io/nj-history-daily"
).rstrip("/")
ET.register_namespace("atom", "http://www.w3.org/2005/Atom")

def main():
    now = datetime.now(ZoneInfo("America/New_York"))
    today_key = now.strftime("%m-%d")
    records = json.loads((ROOT / "history.json").read_text(encoding="utf-8"))
    todays = [item for item in records if item["date"] == today_key]

    rss = ET.Element("rss", {"version": "2.0"})
    channel = ET.SubElement(rss, "channel")
    ET.SubElement(channel, "title").text = "This Day in New Jersey History"
    ET.SubElement(channel, "link").text = SITE_URL
    ET.SubElement(channel, "description").text = (
        "A daily, date-specific New Jersey history feature for community television."
    )
    ET.SubElement(channel, "language").text = "en-us"
    ET.SubElement(channel, "lastBuildDate").text = format_datetime(now)

    if todays:
        for item in todays:
            title = f'This Day in New Jersey History — {now.strftime("%B")} {now.day}: {item["title"]}'
            description = (
                f'{item["text"]} '
                f'Source: {item["source"]} ({item["source_url"]})'
            )
            guid = f'{SITE_URL}/#{now.strftime("%m-%d")}-{item["year"]}'
            entry = ET.SubElement(channel, "item")
            ET.SubElement(entry, "title").text = title
            ET.SubElement(entry, "description").text = description
            ET.SubElement(entry, "link").text = item["source_url"]
            ET.SubElement(entry, "guid", {"isPermaLink": "false"}).text = guid
            ET.SubElement(entry, "pubDate").text = format_datetime(now)
    else:
        entry = ET.SubElement(channel, "item")
        ET.SubElement(entry, "title").text = "This Day in New Jersey History"
        ET.SubElement(entry, "description").text = (
            "Today's New Jersey history entry is being researched and will be added "
            "to the daily archive. Visit the New Jersey State Archives for more history: "
            "https://www.nj.gov/state/archives/"
        )
        ET.SubElement(entry, "guid", {"isPermaLink": "false"}).text = (
            f'{SITE_URL}/#pending-{today_key}'
        )
        ET.SubElement(entry, "pubDate").text = format_datetime(now)

    tree = ET.ElementTree(rss)
    ET.indent(tree, space="  ")
    tree.write(ROOT / "feed.xml", encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    main()
