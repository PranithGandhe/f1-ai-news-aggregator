CREATE TABLE IF NOT EXISTS raw_articles (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    link TEXT NOT NULL UNIQUE,
    source TEXT,
    published_date TIMESTAMP,
    content TEXT,
    status TEXT DEFAULT 'new',
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS processed_articles (
    id SERIAL PRIMARY KEY,
    raw_id INTEGER,
    title TEXT,
    source TEXT,
    link TEXT,
    summary TEXT,
    category TEXT,
    published_date TIMESTAMP,
    processed_at TIMESTAMP,
    FOREIGN KEY(raw_id) REFERENCES raw_articles(id)
);