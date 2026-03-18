CREATE TABLE IF NOT EXISTS raw_articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    link TEXT NOT NULL UNIQUE,
    source TEXT,
    published_date TEXT,
    content TEXT,
    status TEXT DEFAULT 'new',
    created_at TEXT
);

CREATE TABLE IF NOT EXISTS processed_articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    raw_id INTEGER,
    title TEXT,
    source TEXT,
    link TEXT,
    summary TEXT,
    category TEXT,
    published_date TEXT,
    processed_at TEXT,
    FOREIGN KEY(raw_id) REFERENCES raw_articles(id)
);