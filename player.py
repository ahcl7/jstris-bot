import PIL.ImageGrab
from piece import *
from collections import deque
from coff import *
from board import *
import keyboard
import time
import random

X = 885
Y = 515
side = 24
class Player:
    def loadNxtPieces(self):
        self.nxt.clear()
        rgb = PIL.ImageGrab.grab().load()
        
        for i in range(5):
            color = rgb[(X + side // 2, Y - ((4 - i) * 3 * side) + side // 2)]
            print(Y - ((4 - i) * 3 * side) + side // 2)
            if (color not in COLORS or COLORS[color] == 'black'):
                color = rgb[(X + side // 2, Y - ((4 - i) * 3 * side) + side // 2 + side)]
                print(Y - ((4 - i) * 3 * side) + side // 2 + side)
            print(color)
            self.nxt.append(PIECES[COLORS[color]])
        for x in self.nxt:
            print(x.id)

    def __init__(self):
        self.q = deque()
        self.board = Board()
        self.nxt = deque()
        self.speed = 0.005

   

    def findOptimalMove(self, nxt_piece, coff):
        #try to drop piece so that at least hole as possible
        # print(self.board[0][0])


        # print('Before')
        # self.out(self.board)
        
        rotate = 0
        dirs = [0, 1, -1, 2]
        bestValue = 10 ** 5
        bestDir = -1
        bestDelta = -1
        for dir in dirs:
            rotated_piece = nxt_piece.rotate(type=dir)
            for delta in range(-5, 6, 1):
                ok = Board.check_delta(rotated_piece, delta)
                if (ok):
                    new_board, rem = self.board.drop(rotated_piece, delta)  
                    # self.out(new_board)  
                    val = new_board.evaluate(len(rem), coff, abs(dir) + abs(delta))
                    # print(dir, delta, holes, maxHeight)
                    if (val < bestValue):
                        bestValue = val
                        bestDir = dir
                        bestDelta = delta
        # print(bestHolesCnt, bestHeight)

        rotated_piece = nxt_piece.rotate(type = bestDir)
        new_board, rem = self.board.drop(rotated_piece, bestDelta)
        # print('After')
        # new_board.out()
        return bestDir, bestDelta
    def findOptimalMoveWithLookAhead(self, nxt_piece, look_ahead_piece, coff):
        all_nxt_piece = [nxt_piece] + look_ahead_piece
        bestScore = 10 ** 5
        bestDirs = [0] * len(all_nxt_piece)
        bestDeltals = [0] * len(all_nxt_piece)
        bestDir = -1
        bestDelta = -1
        cnt = 0
        start_t = time.time()
        LIM = 1000
        first_step_cnt = 0
        def find(cur, board, removed):
            nonlocal bestScore
            nonlocal bestDir
            nonlocal bestDelta
            nonlocal cnt
            nonlocal first_step_cnt
            nonlocal LIM
            nonlocal coff
            if (cur == len(all_nxt_piece)):
                score = board.evaluate(removed, coff)
                if (score < bestScore):
                    bestScore = score
                    bestDir = bestDirs[0]
                    bestDelta = bestDeltals[0]
                return

            dirs = all_nxt_piece[cur].getDirs()
            if (cur == 0):
                for dir in dirs:
                    rotated_piece = all_nxt_piece[cur].rotate(type=dir)
                    first_step_cnt += len(rotated_piece.getRange(BOARD_WIDTH))
                for dir in dirs:
                    rotated_piece = all_nxt_piece[cur].rotate(type=dir)
                    for delta in rotated_piece.getRange(BOARD_WIDTH):
                        # ok = Board.check_delta(rotated_piece, delta)
                        # if (ok):
                        cnt += 1
                        new_board, rem = board.drop(rotated_piece, delta)  
                        bestDirs[cur] = dir
                        bestDeltals[cur] = delta
                        find(cur + 1, new_board, removed + len(rem))
            else:
                poss = []
                for dir in dirs:
                    rotated_piece = all_nxt_piece[cur].rotate(type = dir)
                    for delta in rotated_piece.getRange(BOARD_WIDTH):
                        poss.append((dir, delta))
                random.shuffle(poss)
                # print('xxxxxxxxxxxxxxxxx', len(poss) , first_step_cnt, LIM // max(1, first_step_cnt))
                for p in poss[0 : LIM // max(1, first_step_cnt)]:
                    dir = p[0]
                    delta = p[1]
                    rotated_piece = all_nxt_piece[cur].rotate(type = dir)
                    new_board, rem = board.drop(rotated_piece, delta)
                    bestDirs[cur] = dir
                    bestDeltals[cur] = delta
                    find(cur + 1, new_board, removed + len(rem))
                    
        find(0, self.board, 0)
        end_t = time.time()
        print('find move time:', (end_t - start_t) * 1000 , 'mssss')
        print(cnt)
        return bestDir, bestDelta

    def play(self):
        def move_right():
            keyboard.press_and_release('right')
            # k = random.randint(1, 2)
            time.sleep(self.speed)
            print('right')
        def move_left():
            keyboard.press_and_release('left') 
            time.sleep(self.speed)
            print('left')
        def hard_drop():
            keyboard.press_and_release('space')
            time.sleep(self.speed)
            print('space')
        def rotate_clockwise():
            keyboard.press_and_release('up')
            time.sleep(self.speed)
            print('up')
        def rotate_counter_clockwise():
            keyboard.press_and_release('z')
            time.sleep(self.speed)
            print('Z')

        # while (self.is_started()):
        #     time.sleep(self.speed)
        # while (not self.is_started()):
        #     time.sleep(self.speed)

        print('Start!!!!')
        
        # print(self.nxt)
        time.sleep(5)
        self.loadNxtPieces()
        hard_drop()
        coff = Coff(17.40749739268519, -4.000590262608939, 5.226413212664031, 1.1900603749418466, 2.3408747677514583)
        while (not self.board.is_dead()):
            self.updateBoard()
            self.board.out()
            dir, delta = self.findOptimalMoveWithLookAhead(self.nxt[0], [self.nxt[1]], coff )
            # dir, delta = self.findOptimalMove(self.nxt[0], coff)
            print(dir, delta)
            if (dir == 1):
                rotate_clockwise()
            if (dir == -1):
                rotate_counter_clockwise()
            if (dir == 2):
                rotate_clockwise()
                rotate_clockwise()
            while (delta < 0):
                move_left()
                delta += 1
            while (delta > 0):
                move_right()
                delta -= 1
            
            self.loadNxtPieces()
            hard_drop()


    def is_started(self):
        self.board.get_board()
        for i in range (BOARD_WIDTH):
            if (self.board.bitmap[0][i]):
                return True
        return False

    def getNxt(self):
        res = -1
        start = time.time()
        rgb = PIL.ImageGrab.grab().load()
        color = rgb[(X + side // 2, Y + side // 2)]
        if  (COLORS[color] == 'black'):
            color = rgb[(X + side // 2, Y + side * 3 / 2)]
        # for i in range(X, X + side):
        #     for j in range(Y, Y + side):
        #         print(findColor(rgb[(i, j)])[0:1], end='')
        #     print()
        self.nxt.append(PIECES[COLORS[color]])

    def updateBoard(self):
        self.board.updateBoard(self.nxt[0])
