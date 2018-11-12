import tkinter
from Tools import *
from ChessItemView import ChessItemView


class ChessView:
    root = tkinter.Tk()
    root.title("Chinese Chess")
    root.resizable(0, 0)
    img = tkinter.PhotoImage(file="images/M_ChessBoard_Board_JDXQ.png")
    can = tkinter.Canvas(root, width=img.width()-68*2, height=img.height()-68*2)
    can.pack(expand=tkinter.YES, fill=tkinter.BOTH)
    can.create_image(-64, -50, image=img, anchor=tkinter.NW)
    piece_images = dict()
    move_images = []

    def draw_board(self, board):
        self.piece_images.clear()
        self.move_images = []
        pieces = board.pieces
        for (x, y) in pieces.keys():
            item = ChessItemView(pieces[x, y])
            self.piece_images[x, y] = item
            self.can.create_image(Tools.board_coord(x), Tools.board_coord(y), image=item.bg)
            self.can.create_image(Tools.board_coord(x), Tools.board_coord(y)-6, image=item.image)
        if board.selected_piece:
            for (x, y) in board.selected_piece.get_move_locs(board):
                self.move_images.append(tkinter.PhotoImage(file="images/OOS.gif"))
                self.can.create_image(Tools.board_coord(x), Tools.board_coord(y), image=self.move_images[-1])

    def showMsg(self, msg):
        self.root.title(msg)

    def __init__(self, control):
        self.control = control
        self.can.bind('<Button-1>', self.control.callback)

    def start(self):
        tkinter.mainloop()
