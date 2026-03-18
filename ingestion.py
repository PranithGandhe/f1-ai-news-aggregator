from database import insert_raw_articles
import feedparser
import json
from datetime import datetime, timedelta, timezone
from dateutil import parser

def load_feeds():
    with open("feeds.json", "r") as f:
        feeds = json.load(f)

    return feeds

def fetch_feed(feed_url):
    feed = feedparser.parse(feed_url)
    return feed

def ingest():
    feeds = load_feeds()

    for feed in feeds:
        source_name = feed["name"]
        feed_url = feed["url"]

        parsed_feed = fetch_feed(feed_url)

        #two_days_ago = datetime.now(timezone.utc) - timedelta(days = 2)

        for entry in parsed_feed.entries:
            title = entry.get("title", "")
            link = entry.get("link", "")
            published_date = entry.get("published", "")
            content = entry.get("summary", "")

            #try:
            #    published_date = parser.parse(published_date)
            #except Exception:
            #    continue

            #if published_date < two_days_ago:
            #   continue

            insert_raw_articles(
                title = title,
                link = link,
                source = source_name,
                published_date = published_date,
                content = content
            )
    print("Ingestion Completed.")