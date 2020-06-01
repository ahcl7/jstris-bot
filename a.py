from player import *


time_lim = 0.1 * 60

#keep board as low as possible
#keep board as least empty cell as possible
#keep the surface as smothy as possible
# machine learning ?? 



#################################################################################

W = 1920
H = 1080




def main():
    print('Started!')
    
    # def testRotate():
    #     def out(piece):
    #         for i in range(len(piece)):
    #             for j in range(len(piece[i])):
    #                 print(1 if piece[i][j] else 0, end='')
    #             print('')
    #     for piece in PIECES:
    #         out(PIECES[piece].rotate(type=1))
    #         print('')
    # def testCounterClockwiseRotate():
    #     def out(piece):
    #         for i in range(len(piece)):
    #             for j in range(len(piece[i])):
    #                 print(1 if piece[i][j] else 0, end='')
    #             print('')
    #     for piece in PIECES:
    #         out(PIECES[piece].rotate(type=-1))
    #         print('')

    def testFindMove():
        player = Player()
        player.nxt.append(P_O)
        player.board.bitmap[0][0] = True
        player.board.bitmap[0][3] = True
        player.board.bitmap[0][4] = True
        player.board.bitmap[0][5] = True
        player.board.bitmap[0][7] = True
        dir, delta = player.findOptimalMove()
        print(dir, delta)

    def testPlay():
        player = Player()
        player.play()

    # testRotate()
    # testCounterClockwiseRotate()
    # player = Player()
    # player.play()
    # player.updateBoard()
    # testFindMove()

    testPlay()

main()