import PIL.ImageGrab
from termcolor import colored
import os
os.system('color')
import time


BOARD_WIDTH = 10
BOARD_HEIGHT = 20
class Board:

    def __init__(self, bitmap = -1):
        if (bitmap == -1):
            self.bitmap = [[False] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
        else:
            self.bitmap = bitmap
    def drop(self, piece, delta):
        start_t = time.time()
        res = [x.copy() for x in self.bitmap]
        bitmap = piece.bitmap
        X = -1
        for h in range(19, -1, -1):
            ok = True
            for i in range (len(bitmap)):
                for j in range(len(bitmap[0])):
                    if (bitmap[i][j]):
                        # print(j + piece.y + delta)
                        ok &= (h >= i and (not self.bitmap[h - i][j + piece.y + delta]))
            if (ok):
                X = h
            else:
                break
        for i in range(len(bitmap)):
            for j in range(len(bitmap[0])):
                #print(X, i)
                if (not bitmap[i][j]): continue
                res[X - i][j + piece.y + delta] |= bitmap[i][j]
        rem = []
        ans = Board([])
        # ans.bitmap = []
        for i in range(BOARD_HEIGHT):
            total = 0
            for j in range(BOARD_WIDTH):
                total += (1 if res[i][j] else 0)
            if (total == BOARD_WIDTH):
                rem.append(i)
            else:
                ans.bitmap.append(res[i])
        
        while (len(ans.bitmap) < BOARD_HEIGHT):
            ans.bitmap.append([False] * BOARD_WIDTH)
        end_t = time.time()
        # print('drop time:', (end_t - start_t) * 1000 , 'mssss')
        return ans, rem

    def out(self):
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                if (self.bitmap[BOARD_HEIGHT - i - 1][j]):
                    print(colored('1', 'red'), ' ', end = '')
                else: print(0, ' ', end='')
            print('')
        print('')

    def get_board(self):
        rgb = PIL.ImageGrab.grab().load()
        X = 590
        Y = 650
        side = 24
        for i in range(20):
            total = 0
            for j in range(10):
                color = rgb[(X + j * side + side // 2, Y - side * i - side // 2)]
                # print(color)
                self.bitmap[i][j] = (color != (0, 0, 0))
                total += 1 if self.bitmap[i][j] else 0
            if (total == 0):
                break

    def updateBoard(self, cur_piece):
        self.get_board()
        # exclude current piece
        # self.out(self.board)
        P = cur_piece
        print(P.id)
        for i in range(19, -1, -1):
            ok = True
            for x in range(P.h):   
                for y in range(P.w):
                    if (not P.bitmap[x][y]): continue
                    if (not self.bitmap[i - x][P.y + y]):
                        ok = False
                        break
            if (ok):
                print("ok" , i)
                for x in range(P.h):   
                    for y in range(P.w):
                        if (not P.bitmap[x][y]): continue
                        self.bitmap[i - x][P.y + y] = not self.bitmap[i - x][P.y + y]
                break
        if (not ok):
            pass

   
    def evaluate(self, line_removed_cnt, coff, step_cnt = 0):
        #it should return a value of board
        #keep board as low as possible
        #surface smoooth 
        #least holes
        #

        # c = [-1] * BOARD_HEIGHT
        # A = 0.00
        # def get_cost(row):
        #     if (c[row] != -1):
        #         return c[row]

        #     res = 0
        #     dependencies = set()
        #     for col in range(BOARD_WIDTH):
        #         if (not self.bitmap[row][col]):
        #             for row1 in range(row+1, BOARD_HEIGHT, 1):
        #                 if row1 in dependencies: continue
        #                 if (self.bitmap[row1][col]):
        #                     dependencies.add(row1)
        #     for dep in dependencies:
        #         res += get_cost(dep) + A
        #     c[row] = res
        #     return res
        if self.is_dead():
            return 10 ** 5
        board = self.bitmap
        holes = 0
        has = [0] * BOARD_WIDTH
        total = 0
        h = [0] * BOARD_WIDTH
        totalHeight = 0
        for i in range(BOARD_HEIGHT - 1, -1, -1):
            for j in range(BOARD_WIDTH):
                if (board[i][j]):
                    h[j] = max(h[j], i)
                    totalHeight += i
                    total += 1
                if (has[j] > 0 and not board[i][j]):
                    holes += 1
                has[j] += 1 if board[i][j] else 0
                
        # empty_cols_cnt = sum([max(0, (BOARD_HEIGHT // 2 - x)) for x in has])
        total = max(total, 1)

        #deep row
        sum_max_height = sum(h)
        # total = max(0, total)
        deep_cnt = 0
        for i in range(BOARD_WIDTH):
            is_deep = False
            if (i > 0 and h[i-1] - h[i] > 2):
                is_deep = True
            if (i + 1 < BOARD_WIDTH and h[i+1] - h[i] > 2):
                is_deep = True
            if (is_deep):
                deep_cnt += 1
        
        diff = 0

        for i in range(1, BOARD_WIDTH):
            diff += abs(h[i] - h[i-1])
        A = 17.72
        return holes * coff.coff_hole + line_removed_cnt * coff.coff_rem + coff.coff_deep ** deep_cnt + totalHeight / total * coff.coff_avg_height + diff * coff.coff_diff
        cost = 0
        # for i in range(BOARD_HEIGHT):
        #     if (c[i] == -1):
        #         cost += get_cost(i)
        # print(cost)
        # return holes * 0.35663+ len(rem) * -0.760666  + sum_max_height * 0.510066 + diff * 0.184483
            
        
    @staticmethod
    def check_delta(piece, delta):
        ok = True
        for i in range(len(piece.bitmap)):
            for j in range(len(piece.bitmap[0])):
                if (piece.bitmap[i][j]):
                    ok &= (j + delta + piece.y >= 0 and j + delta + piece.y < BOARD_WIDTH)
                    if (not ok):
                        break

            if (not ok):
                break
        return ok
    def is_dead(self):
        for i in range(BOARD_WIDTH):
            if (self.bitmap[BOARD_HEIGHT - 1][i]):
                return True
        return False

