import numpy as np

def checkwin(int[] a):
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
                for k in range (i-4, i+5):
                    


                    

    return a



def board(int a):
    # Make array for board
    board_array = np.zeros(a,a, dtype = int)
    return board_array


def turn():





