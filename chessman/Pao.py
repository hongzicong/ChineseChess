
from ChessPiece import ChessPiece


class Pao(ChessPiece):

    def get_image_file_name(self):
        if self.is_red:
            return "images/red3.png"
        else:
            return "images/black3.png"

    def can_move(self, board, dx, dy):
        if dx != 0 and dy != 0:
            return False
        nx, ny = self.x + dx, self.y + dy
        cnt = self.count_pieces(board, self.x, self.y, dx, dy)
        if (nx, ny) not in board.pieces:
            if cnt != 0:
                return False
        else:
            if cnt != 1:
                return False
        return True

    def __init__(self, x, y, is_red):
        ChessPiece.__init__(self, x, y, is_red)

