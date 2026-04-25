INSERT_RAW_ARTICLE:
INSERT INTO raw_articles 
(title, link, source, published_date, content, created_at)
VALUES (%s, %s, %s, %s, %s, %s)
ON CONFLICT (link) DO NOTHING;

GET_UNPROCESSED_ARTICLES:
SELECT * 
FROM raw_articles
WHERE status IN ('new', 'failed');

GET_FAILED_ARTICLES:
SELECT * 
FROM raw_articles
WHERE status = 'failed';

MARK_ARTICLE_PROCESSED:
UPDATE raw_articles
SET status = 'processed'
WHERE id = %s;

MARK_ARTICLE_FAILED:
UPDATE raw_articles
SET status = 'failed'
where id = %s;

INSERT_PROCESSED_ARTICLE:
INSERT INTO processed_articles
(raw_id, title, source, link, summary, category, published_date, processed_at)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);

FLASK_PROCESSED_ARTICLES:
SELECT title, summary, category, source, link, published_date
FROM processed_articles
ORDER BY processed_at DESC
LIMIT 20;

FLASK_CATEGORY_ARTICLES:
SELECT title, summary, category, source, link, published_date
FROM processed_articles
WHERE category = %s
ORDER BY processed_at DESC
LIMIT 20;

GET_LATEST_10:
SELECT *
FROM processed_articles
ORDER BY processed_at DESC
LIMIT 10;