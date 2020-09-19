from app.models.player import Player
import random

class Game:

    def __init__(self):
        self.player1 = None
        self.player2 = None

    def add_player(self,player):
        if self.player1:
            self.player2 = player
        else:
            self.player1 = player

    def cpu_player(self):
        choice = random.randrange(0,2)
        name = random.randrange(0,4)
        names = ["Bart","Lisa","Marge","Homer","Maggie"]
        choices = ["rock","paper","scissors"]
        cpu = Player(names[name],choices[choice])
        return cpu


    def find_winner(self):
        player1 = self.player1.choice.lower()
        player2 = self.player2.choice.lower()
        if player1 == "rock":
            if player2 == "rock":
                return None
            elif player2 == "paper":
                return self.player2.name
            elif player2 == "scissors":
                return self.player1.name
            else:
                return None
        elif player1 == "paper":
            if player2 == "paper":
                return None
            elif player2 == "scissors":
                return self.player2.name
            elif player2 == "rock":
                return self.player1.name
            else:
                return None
        elif player1 == "scissors":
            if player2 == "scissors":
                return None
            elif player2 == "rock":
                return self.player2.name
            elif player2 == "paper":
                return self.player1.name
            else:
                return None
        else:
            return None