import sqlite3
from datetime import datetime
import psycopg2
import os

DATABASE_URL = os.environ.get("DATABASE_URL")

#DB_NAME = "f1_news.db"

def get_connection():
    #conn = sqlite3.connect(DB_NAME)
    #conn.row_factory = sqlite3.Row
    return psycopg2.connect(DATABASE_URL)

#-----------------------------------------------------------------------------------

def load_query(query_name):
    with open("queries.sql", "r") as f:
        content = f.read()
    
    sections = content.split("\n\n")

    for section in sections:
        if section.startswith(query_name):
            return section.split(":", 1)[1].strip()
    
    raise ValueError(f"Query '{query_name}' not found. Please check!!")
    raise ImportError(f"Query '{query_name}' not found. Please check!!")

#-----------------------------------------------------------------------------------

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    with open("schema.sql", "r") as f:
        schema = f.read()

    statements = schema.split(";")

    for x in statements:
        stmt = x.strip()
        if stmt:
            cursor.execute(stmt)

    #cursor.executescript(schema)

    conn.commit()
    conn.close()

#-----------------------------------------------------------------------------------

def insert_raw_articles(title, link, source, published_date, content):
    conn = get_connection()
    cursor = conn.cursor()

    if not published_date or published_date == "":
        published_date = None

    try:
        query = load_query("INSERT_RAW_ARTICLE")

        cursor.execute(query, (
            title,
            link,
            source,
            published_date,
            content,
            datetime.utcnow()
        ))

        conn.commit()

    except sqlite3.IntegrityError:
        print(f"Duplicate article skipped: {title}")

    finally:
        conn.close()

#-----------------------------------------------------------------------------------

def get_unprocessed_articles():
    conn = get_connection()
    cursor = conn.cursor()

    query = load_query("GET_UNPROCESSED_ARTICLES")
    cursor.execute(query)
    
    rows = cursor.fetchall()

    articles = []

    for i in rows:
        articles.append(dict(i))
    
    conn.close()
    return articles

#-----------------------------------------------------------------------------------
'''
def get_failed_articles():
    conn = get_connection()
    cursor = conn.cursor()

    query = load_query("GET_FAILED_ARTICLES")
    cursor.execute(query)
    
    rows = cursor.fetchall()

    articles = []

    for i in rows:
        articles.append(dict(i))
    
    conn.close()
    return articles
'''
#-----------------------------------------------------------------------------------

def mark_article_processed(article_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = load_query("MARK_ARTICLE_PROCESSED")
    cursor.execute(query, (article_id,))

    conn.commit()
    conn.close()
 
#-----------------------------------------------------------------------------------

def mark_article_failed(article_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = load_query("MARK_ARTICLE_FAILED")
    cursor.execute(query, (article_id,))

    conn.commit()
    conn.close()

#-----------------------------------------------------------------------------------

def insert_processed_article(raw_id, title, source, link, summary, category, published_date):
    conn = get_connection()
    cursor = conn.cursor()
    
    query = load_query("INSERT_PROCESSED_ARTICLE")
    
    if not published_date or published_date == "":
        published_date = None

    cursor.execute(query, (
        raw_id,
        title,
        source,
        link,
        summary,
        category,
        published_date,
        datetime.utcnow()
    ))

    conn.commit()
    conn.close()