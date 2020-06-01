from player import *
from piece import *
import random
import time

class Game:
    def __init__(self):
        self.player = Player()

    def play(self, ):
        cnt = 0
        random.seed(0)
        ps = [PIECES[x] for x in PIECES]

        used = [0] * 7
        cnt1 = 0
        id = 7
        nxt_piece = PIECES[random.choice([x for x in PIECES])]
        while (not self.player.board.is_dead()):
            if (id == 7):
                random.shuffle(ps)
                id = 0
            self.player.board.out()
            nxt_piece1 = PIECES[random.choice([x for x in PIECES])]
            # nxt_piece = ps[id]
            # print(nxt_piece.id)
            used[nxt_piece.id] += 1
            nxt_piece.out()
            self.player.nxt.append(nxt_piece)
            dir, delta = self.player.findOptimalMoveWithLookAhead(nxt_piece, [nxt_piece1])
            self.player.board , rem = self.player.board.drop(nxt_piece.rotate(dir), delta)
            # print(player.board)
            self.player.nxt.clear()
            cnt1 += len(rem)
            id += 1
            nxt_piece = nxt_piece1
        cnt += cnt1
        return cnt
    def playWithoutLookingAhead(self, coff):
        cnt = 0
        random.seed(0)
        ps = [PIECES[x] for x in PIECES]

        used = [0] * 7
        cnt1 = 0
        id = 7
        nxt_piece = PIECES[random.choice([x for x in PIECES])]
        while (not self.player.board.is_dead()):
            if (id == 7):
                random.shuffle(ps)
                id = 0
            # self.player.board.out()
            nxt_piece1 = PIECES[random.choice([x for x in PIECES])]
            # nxt_piece = ps[id]
            # print(nxt_piece.id)
            used[nxt_piece.id] += 1
            # nxt_piece.out()
            self.player.nxt.append(nxt_piece)
            dir, delta = self.player.findOptimalMove(nxt_piece, coff)
            self.player.board , rem = self.player.board.drop(nxt_piece.rotate(dir), delta)
            # print(player.board)
            self.player.nxt.clear()
            cnt1 += len(rem)
            id += 1
            nxt_piece = nxt_piece1
        cnt += cnt1
        return cnt