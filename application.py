from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def welcome_page():
    # ! render front end template
    app.logger.debug("received request...")
    return render_template("index.html",name="Shilpa")

@app.get("/search/<query>")
def search_movie_plot(query):
    # ! all search request will come here
    return [{"movie_name":"Maa Kasam","plot":"A person takes revenge for death of his mother."}]