from database import (
    get_unprocessed_articles,
    mark_article_failed,
    mark_article_processed,
    insert_processed_article
)
from summarizer import summarize
from categorizer import categorize

def process_articles():

    articles = get_unprocessed_articles()

    for article in articles:

        try:
            title = article["title"]
            content = article["content"]
            source = article["source"]
            link = article["link"]
            summary = summarize(content)
            category = categorize(title, content)
            #published_date = article["published_date"]

            print(f"Processed: {title}")
            print(f"Category: {category}")

            published_date = article.get("published_date")

            if not published_date or published_date == "":
                published_date = None

            insert_processed_article(
                raw_id = article["id"],
                title = title,
                source =  source,
                link = link,
                summary = summary,
                category = category,
                published_date = published_date
                )
            
            mark_article_processed(article["id"])
            print(f"Processed: {title}")

        except Exception as e:
            print(f"Processing failed for article {article['id']}: {e}")
            mark_article_failed(article["id"])