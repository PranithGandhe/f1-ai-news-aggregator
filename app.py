from database import load_query, get_connection, initialize_database
from flask import Flask, render_template
import os
from pipeline import run_pipeline
from datetime import datetime, timezone



#initialize_database()
#run_pipeline()

app = Flask(__name__)

@app.route("/run-pipeline")
def trigger_pipeline():
    from database import initialize_database
    from pipeline import run_pipeline

    initialize_database()
    run_pipeline()

    return "Pipeline is triggered."


@app.route("/")
def home():

    conn = get_connection()
    cursor = conn.cursor()

    query = load_query("FLASK_PROCESSED_ARTICLES")
    cursor.execute(query)

    rows = cursor.fetchall()

    '''print(type(articles))
    print(type(articles[0]))
    print(articles[0])'''

    columns = [col[0] for col in cursor.description]
    articles = [dict(zip(columns, row)) for row in rows]

    conn.close()

    return render_template(
        "index.html", 
        articles = articles,
        page_title = "Latest F1 News",
        time_ago = time_ago)

@app.route("/category/<category>")
def category_page(category):

    conn = get_connection()
    cursor = conn.cursor()

    query = load_query("FLASK_CATEGORY_ARTICLES")
    cursor.execute(query, (category,))

    rows = cursor.fetchall()

    columns = [col[0] for col in cursor.description]
    articles = [dict(zip(columns, row)) for row in rows]

    conn.close()

    return render_template(
        "index.html", 
        articles = articles, 
        page_title = category,
        time_ago = time_ago)

def time_ago(published_date):
    if not published_date:
        return "Unknown"

    now = datetime.now(timezone.utc)

    if isinstance(published_date, str):
        published_date = datetime.fromisoformat(published_date)

    if published_date.tzinfo is None:
        published_date = published_date.replace(tzinfo=timezone.utc)
    
    diff = now - published_date

    seconds = diff.total_seconds()

    if seconds < 60:
        return "Just now"
    elif seconds < 3600:
        return f"{int(seconds // 60)} min ago"
    elif seconds < 86400:
        return f"{int(seconds // 3600)} hrs ago"
    elif seconds < 172800:
        return "Yesterday"
    else:
        return f"{int(seconds // 86400)} days ago"


if __name__ == "__main__":
    #app.run(debug = True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)