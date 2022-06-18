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
    value = True
    return render_template("index.html", value=value)


@app.route("/game")
def game():
    value = True
    return render_template("game_start.html", value=value)


@app.route("/create_game")
def create_game():
    value = True
    return render_template("create_game.html", value=value)


@app.route("/join_game")
def join_game():
    value = True
    return render_template("join_game.html", value=value)



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


@app.route("/view1")
def view1():
    return render_template("view1.html")


@app.route("/view2")
def view2():
    return render_template("view2.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True
    )