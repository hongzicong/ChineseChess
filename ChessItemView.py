import tkinter

class ChessItemView:
    def __init__(self, chess):
        self.image = tkinter.PhotoImage(file=chess.get_image_file_name())
        self.bg = tkinter.PhotoImage(file="images/chess.png")
