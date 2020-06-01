from termcolor import colored
class Piece:
    def __init__(self, id, bitmap):
        self.id = id
        self.bitmap = list(map(lambda arr: [True if x == 1 else False for x in arr], bitmap))
        self.y = 3
        self.h = len(bitmap)
        self.w = len(bitmap[0])

    def out(self):
        for i in range(self.h):
            for j in range(self.w):
                if (self.bitmap[i][j]):
                    print(colored('1', 'red'), end = '')
                else:
                    print(' ', end = '')
            print('')
            
    def rotate_clockwise(self):
        if (self.id == 5):
            return self.bitmap.copy()
        res = [[False] * self.w for _ in range(self.h)]
        for i in range(self.h):
            for j in range(self.w):
                res[j][self.h - i - 1] = self.bitmap[i][j]
        return res

    def rotate_counter_clockwise(self):
        # print(self.id)
        if (self.id == 5):
            return self.bitmap.copy()
        res = [[False] * self.w for _ in range(self.h)]
        for i in range(self.h):
            for j in range(self.w):
                res[self.h - j - 1][i] = self.bitmap[i][j]
        return res

    def rotate(self, type = 0):
        res = Piece(self.id, self.bitmap)
        if (type == -1):
            res.bitmap = self.rotate_counter_clockwise()
        if (type == 1):
            res.bitmap = self.rotate_clockwise()
        if (type == 2):
            if (self.id == 4 or self.id == 3):
                return self.rotate(type = 1).rotate(type = 1)   
        return res
    def getRange(self, w):
        l = 100
        r = -1
        for i in range(self.h):
            for j in range(self.w):
                if (self.bitmap[i][j]):
                    l = min(l, j)
                    r = max(r, j)
        return range(-l - self.y, w - r - self.y)
    def getDirs(self):
        if (self.id == 5):
            return [0]
        elif (self.id in {3, 4}):
            return [0, -1, 1, 2]
        else:
            return [0, -1, 1]

P_Z1 = Piece(0, [
    [0, 1, 1],
    [1, 1, 0],
    [0, 0, 0]
])

P_Z2 = Piece(1, [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 0]
])

P_T = Piece(2, [
    [0, 1, 0],
    [1, 1, 1],
    [0, 0, 0]
])

P_L1 = Piece(3, [
    [1, 0, 0],
    [1, 1, 1],
    [0, 0, 0]
])

P_L2 = Piece(4, [
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
])

P_O = Piece(5, [
    [0, 1, 1],
    [0, 1, 1],
    [0, 0, 0]
])

P_I = Piece(6, [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
])

COLORS = {
    (15, 155, 215) : 'cyan',
    (227, 91, 2): 'organge',
    (175, 41, 138): 'pink',
    (89, 177, 1): 'green',
    (215, 15, 55): 'red',
    (33, 65, 198): 'blue',
    (227, 159, 2): 'yellow',
    (0, 0, 0): 'black',
    (30, 30, 30): 'black',
    (34, 34, 34): 'black'
}

PIECES = {
    'cyan': P_I,
    'organge': P_L2,
    'pink': P_T,
    'green': P_Z1,
    'red': P_Z2,
    'blue': P_L1,
    'yellow': P_O
}


if __name__ == '__main__':
    print(P_L1.rotate(2).bitmap)
