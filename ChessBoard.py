from chessman.Bing import *
from chessman.Shuai import *
from chessman.Pao import *
from chessman.Shi import *
from chessman.Xiang import *
from chessman.Ma import *
from chessman.Che import *
import copy


class ChessBoard:

    # used to fast access
    black_pieces = dict()
    red_pieces = dict()

    pieces = dict()


    pieces[4, 0] = red_pieces[4, 0] = Shuai(4, 0, True)
    pieces[0, 3] = red_pieces[0, 3] = Bing(0, 3, True)
    pieces[2, 3] = red_pieces[2, 3] = Bing(2, 3, True)
    pieces[4, 3] = red_pieces[4, 3] = Bing(4, 3, True)
    pieces[6, 3] = red_pieces[6, 3] = Bing(6, 3, True)
    pieces[8, 3] = red_pieces[8, 3] = Bing(8, 3, True)
    pieces[1, 2] = red_pieces[1, 2] = Pao(1, 2, True)
    pieces[7, 2] = red_pieces[7, 2] = Pao(7, 2, True)
    pieces[3, 0] = red_pieces[3, 0] = Shi(3, 0, True)
    pieces[5, 0] = red_pieces[5, 0] = Shi(5, 0, True)
    pieces[2, 0] = red_pieces[2, 0] = Xiang(2, 0, True)
    pieces[6, 0] = red_pieces[6, 0] = Xiang(6, 0, True)
    

    pieces[1, 0] = red_pieces[1, 0] = Ma(1, 0, True)
    pieces[7, 0] = red_pieces[7, 0] = Ma(7, 0, True)
    
    pieces[0, 0] = red_pieces[0, 0] = Che(0, 0, True)

    pieces[8, 0] = red_pieces[8, 0] = Che(8, 0, True)


    pieces[4, 9] = black_pieces[4, 9] = Shuai(4, 9, False)
    pieces[0, 6] = black_pieces[0, 6] = Bing(0, 6, False)
    pieces[2, 6] = black_pieces[2, 6] = Bing(2, 6, False)
    pieces[4, 6] = black_pieces[4, 6] = Bing(4, 6, False)
    pieces[6, 6] = black_pieces[6, 6] = Bing(6, 6, False)
    pieces[8, 6] = black_pieces[8, 6] = Bing(8, 6, False)
    pieces[1, 7] = black_pieces[1, 7] = Pao(1, 7, False)
    pieces[7, 7] = black_pieces[7, 7] = Pao(7, 7, False)
    pieces[3, 9] = black_pieces[3, 9] = Shi(3, 9, False)
    pieces[5, 9] = black_pieces[5, 9] = Shi(5, 9, False)
    pieces[2, 9] = black_pieces[2, 9] = Xiang(2, 9, False)
    pieces[6, 9] = black_pieces[6, 9] = Xiang(6, 9, False)
    
    pieces[1, 9] = black_pieces[1, 9] = Ma(1, 9, False)
    pieces[7, 9] = black_pieces[7, 9] = Ma(7, 9, False)
    pieces[0, 9] = black_pieces[0, 9] = Che(0, 9, False)

    pieces[8, 9] = black_pieces[8, 9] = Che(8, 9, False)

    selected_piece = None

    def __init__(self):
        pass

    def can_move(self, x, y, dx, dy):
        return self.pieces[x, y].can_move(self, dx, dy)

    def move(self, x, y, dx, dy):
        nx, ny = x + dx, y + dy

        # kill another chess piece
        if (nx, ny) in self.pieces:
            if self.pieces[nx, ny].is_red:
                del self.red_pieces[nx, ny]
            else:
                del self.black_pieces[nx, ny]
            del self.pieces[nx, ny]

        self.pieces[nx, ny] = self.pieces[x, y]
        self.pieces[nx, ny].x = nx
        self.pieces[nx, ny].y = ny

        del self.pieces[x, y]

        if self.pieces[nx, ny].is_red:
            del self.red_pieces[x, y]
            self.red_pieces[nx, ny] = self.pieces[nx, ny]
        else:
            del self.black_pieces[x, y]
            self.black_pieces[nx, ny] = self.pieces[nx, ny]

    def select(self, x, y, player_is_red):
        if not self.selected_piece:
            if (x, y) in self.pieces and self.pieces[x, y].is_red == player_is_red:
                self.pieces[x, y].selected = True
                self.selected_piece = self.pieces[x, y]
            return False

        if not (x, y) in self.pieces:
            if self.selected_piece:
                ox, oy = self.selected_piece.x, self.selected_piece.y
                if self.can_move(ox, oy, x - ox, y - oy):
                    self.move(ox, oy, x-ox, y-oy)
                    self.pieces[x, y].selected = False
                    self.selected_piece = None
                    return True
            return False

        if self.pieces[x, y].selected:
            return False

        if self.pieces[x, y].is_red != player_is_red:
            ox, oy = self.selected_piece.x, self.selected_piece.y
            if self.can_move(ox, oy, x - ox, y - oy):
                self.move(ox, oy, x - ox, y - oy)
                self.pieces[x, y].selected = False
                self.selected_piece = None
                return True
            return False
        for key in self.pieces.keys():
            self.pieces[key].selected = False
        self.pieces[x, y].selected = True
        self.selected_piece = self.pieces[x, y]
        return False

    def fake_move(self, x, y, dx, dy):
        newboard = ChessBoard()
        newboard.pieces = dict()
        newboard.red_pieces = dict()
        newboard.black_pieces = dict()

        for (temp_x, temp_y) in self.pieces:
            if self.pieces[temp_x, temp_y].is_red:
                newboard.red_pieces[temp_x, temp_y] = newboard.pieces[temp_x, temp_y] = copy.deepcopy(self.pieces[temp_x, temp_y])
            else:
                newboard.black_pieces[temp_x, temp_y] = newboard.pieces[temp_x, temp_y] = copy.deepcopy(self.pieces[temp_x, temp_y])

        nx, ny = x + dx, y + dy

        # kill another chess piece
        if (nx, ny) in newboard.pieces:
            if newboard.pieces[nx, ny].is_red:
                del newboard.red_pieces[nx, ny]
            else:
                del newboard.black_pieces[nx, ny]
            del newboard.pieces[nx, ny]

        newboard.pieces[nx, ny] = newboard.pieces[x, y]
        newboard.pieces[nx, ny].x = nx
        newboard.pieces[nx, ny].y = ny

        del newboard.pieces[x, y]

        if newboard.pieces[nx, ny].is_red:
            del newboard.red_pieces[x, y]
            newboard.red_pieces[nx, ny] = newboard.pieces[nx, ny]
        else:
            del newboard.black_pieces[x, y]
            newboard.black_pieces[nx, ny] = newboard.pieces[nx, ny]

        return newboard
