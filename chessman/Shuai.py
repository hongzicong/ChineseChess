from ChessPiece import ChessPiece


class Shuai(ChessPiece):

    is_king = True
    def get_image_file_name(self):
        if self.is_red:
            return "images/red5.png"
        else:
            return "images/black5.png"


    def can_move(self, board, dx, dy):
        nx, ny = self.x + dx, self.y + dy
        if dx == 0 and self.count_pieces(board, self.x, self.y, dx, dy) == 0 and ((nx, ny) in board.pieces) and board.pieces[nx, ny].is_king:
            return True
        if not (self.is_red and 3 <= nx <=5 and 0<= ny <=2) and not (self.is_red == False and 3 <= nx <= 5 and 7 <= ny <= 9):
            return False
        if abs(dx) + abs(dy) !=1:
            #print 'too far'
            return False
        return True

    def __init__(self, x, y, is_red):
        ChessPiece.__init__(self, x, y, is_red)

