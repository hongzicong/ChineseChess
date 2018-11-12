from Tools import *
from ChessBoard import *
from AI import AI
from ChessView import ChessView
import time


class ChessGame:

    def __init__(self):
        self.board = ChessBoard()
        self.view = ChessView(self)
        self.view.showMsg("Red")
        self.view.draw_board(self.board)
        self.player_is_red = True
        self.ai = AI()

    def start(self):
        self.view.start()

    def callback(self, event):
        rx, ry = Tools.real_coord(event.x), Tools.real_coord(event.y)
        if self.board.select(rx, ry, self.player_is_red):
            self.player_is_red = not self.player_is_red
            self.view.showMsg("Red" if self.player_is_red else "Green")
        self.view.draw_board(self.board)

        # the round of AI
        time.sleep(1)
        self.ai.go_next_step(self.board)
        self.player_is_red = not self.player_is_red
        self.view.showMsg("Red" if self.player_is_red else "Green")
        self.view.draw_board(self.board)


game = ChessGame()
game.start()
