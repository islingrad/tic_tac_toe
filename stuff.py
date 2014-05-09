from board import *
import os
game_board = board()
def check_input(player):
    while True:
        hey_you = raw_input(player +"'s move")
        try:
            int(hey_you)
            return int(hey_you)
            break
        except ValueError:
            continue

def game_init():
    while True:
        game_board.display()
        game_board.make_move("x")
        game_board.win_test()
        os.system('cls')
        game_board.display()
        game_board.make_move("o")
        game_board.win_test()
        os.system('cls')
