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

gamePage = False


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/game")
def game():
    return render_template("game_start.html")


@app.route("/create_game")
def create_game():
    return render_template("create_game.html")


@app.route("/join_game")
def join_game():
    return render_template("join_game.html")


# *********** Game Pages *************


@app.route("/entrance")
def entrance():
    gamePage = True
    return render_template("entrance.html", gamePage=gamePage)


@app.route("/hallway")
def hallway():
    gamePage = True
    return render_template("hallway.html", gamePage=gamePage)


@app.route("/patio")
def patio():
    gamePage = True
    return render_template("patio.html", gamePage=gamePage)


@app.route("/bedroom")
def bedroom():
    gamePage = True
    return render_template("bedroom.html", gamePage=gamePage)


@app.route("/lounge")
def lounge():
    gamePage = True
    return render_template("lounge.html", gamePage=gamePage)


@app.route("/view1")
def view1():
    gamePage = True
    return render_template("view1.html", gamePage=gamePage)


@app.route("/view2")
def view2():
    gamePage = True
    return render_template("view2.html", gamePage=gamePage)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True
    )