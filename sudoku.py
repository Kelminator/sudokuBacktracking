import timeit
import matplotlib.pyplot as plot
board =  [
    [0,0,0,8,0,1,0,0,0],
    [0,0,0,0,0,0,0,4,3],
    [5,0,0,0,0,0,0,0,0],
    [0,0,0,0,7,0,8,0,0],
    [0,0,0,0,0,0,1,0,0],
    [0,2,0,0,3,0,0,0,0],
    [6,0,0,0,0,0,0,7,5],
    [0,0,3,4,0,0,0,0,0],
    [0,0,0,2,0,0,6,0,0],
          ]


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")



def sudoku(board):
    empty = emptySlot(board)
    if not empty:
        return True
    else:
        row, col = empty
        for i in range(1,10):
            if isValidEntry((row, col), board, i):
                board[row][col] = i
                if sudoku(board):
                    return True

            board[row][col] = 0

        return False


def emptySlot(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i, j  #row, col
    return None

def isValidEntry(pos, board, number):
    # is it valid in the row
    for j in range(len(board[0])):
        if board[pos[0]][j] == number and pos[1] != j:
            return False
    # is it valid in the col
    for i in range(len(board[1])):
        if board[i][pos[1]] == number and pos[0] != i:
            return False
    # is it valid in the square
    box_col = pos[1] // 3
    box_row = pos[0] // 3
    for i in range(box_row*3, box_row*3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == number and (i, j) != pos:
                return False
    return True



def sudoku1(board, roww, coll):
    empty = emptySlot1(board, roww, coll)
    if not empty:
        return True
    else:
        row, col = empty
        roww, coll = empty
        for i in range(1,10):
            if isValidEntry1((row, col), board, i):
                board[row][col] = i
                if sudoku1(board, roww, coll):
                    return True

            board[row][col] = 0

        return False


def emptySlot1(board, row, col):
    for i in range(row, len(board)):
        if i > row:
            for j in range(len(board)):
                if board[i][j] == 0:
                    return i, j  # row, col
        else:
            for j in range(col, len(board)):
                if board[i][j] == 0:
                    return i, j  # row, col
    return None

def isValidEntry1(pos, board, number):
    # is it valid in the row
    for j in range(len(board[0])):
        if board[pos[0]][j] == number and pos[1] != j:
            return False
    # is it valid in the col
    for i in range(len(board[1])):
        if board[i][pos[1]] == number and pos[0] != i:
            return False
    # is it valid in the square
    box_col = pos[1] // 3
    box_row = pos[0] // 3
    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == number and (i, j) != pos:
                return False
    return True



s_timer = []

# start = timeit.default_timer()
# sudoku(board)
# stop = timeit.default_timer()
# s_timer.append(stop - start)

start1 = timeit.default_timer()
sudoku1(board, 0, 0)
stop1 = timeit.default_timer()
s_timer.append(stop1 - start1)
print(s_timer)


# s = ['double for loop', 'modified for loop']
# plot.plot(s, s_timer)
# plot.ylabel('Time')
# plot.xlabel('version')
# plot.show()
