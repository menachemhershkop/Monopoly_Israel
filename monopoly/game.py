from monopoly.board import Board
from monopoly.dice import Dice
from monopoly.player import Player



def run_game():
    step=20
    board = Board()
    player1=Player("dani",0,1500)
    player2=Player("computer",0,1500)
    cube=Dice
    while step:
        player1.location=board.movement(cube.Throwing_a_die())
        print(player1.location)
        break

