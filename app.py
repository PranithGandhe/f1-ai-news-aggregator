from database import load_query, get_connection
from flask import Flask, render_template
import os

app = Flask(__name__)

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

    return render_template("index.html", articles = articles)

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

    return render_template("index.html", articles = articles, page_title = category)

if __name__ == "__main__":
    #app.run(debug = True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)