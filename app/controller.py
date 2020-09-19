from flask import render_template, request
from app import app
from app.models.player import Player
from app.models.game import Game

@app.route('/')
def index():
    return render_template("index.html",title="home")

@app.route('/twoplayer', methods=['POST'])
def two_player():
    # create player 1
    p1name = request.form["p1-name"]
    p1choice = request.form["p1-move"]
    player1 = Player(p1name,p1choice)
    # Create player 2
    p2name = request.form["p2-name"]
    p2choice = request.form["p2-move"]
    player2 = Player(p2name,p2choice)
    # create game and add players
    game1 = Game()
    game1.add_player(player1)
    game1.add_player(player2)
    # find winner
    winner = game1.find_winner()
    return render_template("result.html",title="FIGHT OVER",winner=winner,game=game1)   

@app.route('/oneplayer')
def load_one_player():
    return render_template("oneplayer.html",title="One Player Mode")

@app.route('/oneplayer/game/', methods=['POST'])
def one_player():
    # create game
    game1 = Game()
    # create player one (human)
    p1name = request.form["p1-name"]
    p1move = request.form["p1-move"]
    player1 = Player(p1name,p1move)
    # create player two (Computer)
    player2 = game1.cpu_player()
    # add players to game
    game1.add_player(player1)
    game1.add_player(player2)
    # find winner
    winner = game1.find_winner()
    return render_template("result.html",title="FIGHT OVER",winner=winner,game=game1)