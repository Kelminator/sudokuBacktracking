#Solves the sudoku board, using backtracking
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
