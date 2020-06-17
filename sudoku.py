import timeit
import matplotlib.pyplot as plot

board = [
    [2,3,0,6,0,0,0,0,1],
    [0,0,1,9,8,0,7,6,0],
    [9,0,0,1,0,5,4,0,2],
    [7,0,2,3,1,8,0,4,0],
    [8,0,6,0,5,0,3,1,7],
    [0,1,5,0,7,6,2,9,8],
    [0,0,0,7,0,4,0,2,0],
    [6,0,0,0,0,0,8,3,0],
    [1,0,4,0,0,0,5,0,0],
          ]

board2 = [
    [2,3,0,6,0,0,0,0,1],
    [0,0,1,9,8,0,7,6,0],
    [9,0,0,1,0,5,4,0,2],
    [7,0,2,3,1,8,0,4,0],
    [8,0,6,0,5,0,3,1,7],
    [0,1,5,0,7,6,2,9,8],
    [0,0,0,7,0,4,0,2,0],
    [6,0,0,0,0,0,8,3,0],
    [1,0,4,0,0,0,5,0,0],
          ]

#Prints the board
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


#Solves the sudoku board, using backtracking
def solverNSqrd(board):
    empty = emptySlotNSqrd(board)
    if not empty:
        return True
    else:
        row, col = empty
        for i in range(1,10):
            if isValidEntry((row, col), board, i):
                board[row][col] = i
                if solverNSqrd(board):
                    return True

            board[row][col] = 0

        return False

#Locates the first empty square on the board in N^2 time
def emptySlotNSqrd(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i, j  #row, col
    return None

#Verifies that the position a given number is placed does not "break the board" aka is still considered a viable answer
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


def solverModified(board, roww, coll):
    empty = emptySlotModified(board, roww, coll)
    if not empty:
        return True
    else:
        row, col = empty
        roww, coll = empty
        for i in range(1,10):
            if isValidEntry((row, col), board, i):
                board[row][col] = i
                if solverModified(board, roww, coll):
                    return True

            board[row][col] = 0

        return False

#Locates the first empty square on the board in N^2 time but with a modification to start at where it left off
def emptySlotModified(board, row, col):
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


#generates a visual aid for to see the difference in run time.
print("Unsolved board:")
print_board(board)
print("")
print("Solved board:")

s_timer = []
start = timeit.default_timer()
solverNSqrd(board)
stop = timeit.default_timer()
s_timer.append(stop - start)
start1 = timeit.default_timer()
solverModified(board2, 0, 0)
stop1 = timeit.default_timer()
s_timer.append(stop1 - start1)

print_board(board2)
print("")

print("run Times, solverNSqrd: " + str(s_timer[0]) + " solverModified: " + str(s_timer[1]))


s = ['double for loop', 'modified for loop']
plot.plot(s, s_timer)
plot.ylabel('Time')
plot.xlabel('version')
plot.show()

