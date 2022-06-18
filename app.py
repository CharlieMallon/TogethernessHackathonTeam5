import os
from flask import (
    Flask, config, render_template,
    redirect, request, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/game")
def game():
    return render_template("game.html")


@app.route("/entrance")
def entrance():
    return render_template("entrance.html")


@app.route("/hallway")
def hallway():
    return render_template("hallway.html")


@app.route("/patio")
def patio():
    return render_template("patio.html")


@app.route("/bedroom")
def bedroom():
    return render_template("bedroom.html")


@app.route("/lounge")
def lounge():
    return render_template("lounge.html")


@app.route("/veiw1")
def veiw1():
    return render_template("veiw1.html")


@app.route("/veiw2")
def veiw2():
    return render_template("veiw2.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True
    )