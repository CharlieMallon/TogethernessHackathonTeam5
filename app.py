from html import entities
import os
from pickle import TRUE
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
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


@app.route("/create_game", methods=['GET', 'POST'])
def create_game():
    if request.method == 'POST':
        game_id = request.form.get("game_ID").lower()
        if request.form.get("player_no"):
            player_two = request.form.get("player_name").lower()
            player_one = ""
            player = 2
        else:
            player_one = request.form.get("player_name").lower()
            player_two = ""
            player = 1

        if request.form.get("private"):
            private = True
        else:
            private = False

        game = {
            "game_id": game_id,
            "private": private,
            "player_one": player_one,
            "player_two": player_two,
        }
        try:
            mongo.db.games.insert_one(game)
            mongo.db.game_text.insert_one({
                "game_id": game_id,
                "entries": [],
            })
            session["game_id"] = game_id
            session["player_no"] = player
            return redirect(url_for('entrance'))
        except:
            print("error")

    return render_template("create_game.html")


@app.route("/find_game", methods=['GET', 'POST'])
def find_game():
    games = mongo.db.games.find()
    
    if request.method == 'POST':
        game_id = request.form.get("game_id").lower()
        session["game_id"] = game_id
        return redirect(url_for('join_game'))
    return render_template("find_game.html", games=games)

@app.route("/join_game", methods=['GET', 'POST'])
def join_game():
    game = mongo.db.games.find_one({
        "game_id": session["game_id"],
        })
    if game["player_one"] == "":
        player = 1
    else:
        player = 2
    session["player_no"] = player

    if request.method == 'POST':
        find = { 'game_id': session["game_id"]}
        player = session["player_no"]

        if player == 1:
            player_one = request.form.get("player_name").lower()
            player_two = game['player_two']
        else:
            player_one = game['player_one']
            player_two = request.form.get("player_name").lower()

        update = { "$set": {
            "player_one": player_one,
            "player_two": player_two,
            "closed": True
        }}

        mongo.db.games.update_one(find, update)
        return redirect(url_for('entrance'))
    return render_template("join_game.html", game=game)


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
    entries = mongo.db.game_text.find_one(
        {
            "game_id": session["game_id"]
        }, ["entries"]
    )
    print(session["game_id"])
    print()

    return render_template("patio.html", gamePage=gamePage, entries=entries['entries'],
                           current_player=session["player_no"])


@app.route("/entry/<trigger>")
def entry(trigger):
    gamePage = True
    origin = request.args.get('origin', None)
    dialog = mongo.db.dialog.find_one({
        "player": session["player_no"],
        "trigger": trigger
        }, ["dialog"])
    
    entry = {
        "player": session["player_no"],
        "text": dialog["dialog"]
    }
    print(entry)

    game_text = mongo.db.game_text.find_one(
        {
            "game_id": session["game_id"]
        }
    )
    game_text_id = game_text["_id"]
    
    mongo.db.game_text.update_one(
            {"_id": ObjectId(game_text_id)}, {'$push': {'entries': entry}})
    
    entries = mongo.db.game_text.find_one(
        {
            "game_id": session["game_id"]
        }, ["entries"]
    )

    return render_template(f"{origin}.html", gamePage=gamePage, entries=entries, current_player=session["player_no"])


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