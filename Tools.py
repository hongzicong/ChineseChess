class Tools:

    def real_coord(x):
        if x <= 68:
            return 0
        else:
            return int((x-68)/68) + 1


    def board_coord(x):
        return 44 + 68*x