import numpy as np

def checkwin(int[] a, flag):
    for i in range(a):
        for j in range(a):
            if a(i,j) == 1:
                int count = 0
                # 4type of checking process
                # vertical check
                for k in range(i-4,i+5):
                    if a(k,j) == 1:
                        count += 1
                    else:
                        count = 0

                # horizontal check
                for k in range(i-4,i+5):
                    if a(i,k) == 1:
                        count += 1
                    else:
                        count = 0

                # left-up diagonal check
                for k in range(-4, 5):
                    if a(i+k,j+k) == 1:
                        count += 1
                    else:
                        count = 0
                
                # right-up diagonal check
                for k in range(4, -4):
                    if a(i-k, j+k) == 1:
                        count += 1
                    else:
                        count = 0
                
                # check count = 5
                if count == 5:
                    return flag






def board(int a):
    # Make array for board
    board_array = np.zeros(a,a, dtype = int)
    return board_array


def turn():


def setblock(int turn):
    # for black, stone = 1
    if turn == 0:
        input(int a, int b)
        board_array(a,b) = 1
    
    # for white, stone =2
    if turn == 1:
        input(int a, int b)
        board_array(int a, int ,b)






