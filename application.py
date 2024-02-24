from flask import Flask, render_template
import db

app = Flask(__name__)


@app.route("/")
def welcome_page():
    # ! render front end template
    app.logger.debug("received request...")
    return render_template("search.html")


@app.get("/search/<query>")
def search_movie_plot(query):
    app.logger.debug("query to search {query}".format(query=query))
    query = query.strip()
    search_result = db.search_data([query])
    return search_result
