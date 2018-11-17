from Tools import *
from ChessBoard import *
from AI import AI
from ChessView import ChessView


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
            self.view.showMsg("Green")
        self.view.draw_board(self.board)

        if not self.player_is_red:
            # the round of AI
            list_step = self.ai.find_next_step(self.board, 2)
            self.board.select(list_step[1][0][0], list_step[1][0][1], self.player_is_red)
            self.board.select(list_step[1][0][0] + list_step[1][0][2], list_step[1][0][1] + list_step[1][0][3],
                              self.player_is_red)
            self.player_is_red = not self.player_is_red
            self.view.showMsg("Red")
            self.view.draw_board(self.board)


game = ChessGame()
game.start()
