#Reference: Sudoku Generator Algorithm - www.101computing.net/sudoku-generator-algorithm/
from Solver import isValidEntry, emptySlotModified
from random import randint, shuffle

board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
          ]

# A function to check if the board is full
def isFull(board):
    for row in range(0, 9):
        for col in range(0, 9):
            if board[row][col] == 0:
                return False

    return True

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def shuffledBoard(board):
    empty = emptySlotModified(board, 0, 0)
    if not empty:
        return True
    else:
        row, col = empty
        shuffle(numberList)
        for value in numberList:
            if isValidEntry((row, col), board, value):
                board[row][col] = value
                if isFull(board):
                    return True
                else:
                    if shuffledBoard(board):
                        return True
            board[row][col] = 0
        return False


def solvedBoard(board):
    empty = emptySlotModified(board, 0, 0)
    if not empty:
        return True
    else:
        row, col = empty
        for i in range(1, 10):
            if isValidEntry((row, col), board, i):
                board[row][col] = i
                if isFull(board):
                    return True
                else:
                    if solvedBoard(board):
                        return True
            board[row][col] = 0

# Start Removing Numbers one by one

# A higher number of attempts will end up removing more numbers from the grid
# Potentially resulting in more difficiult grids to solve!
def remover(board):
    attempts = randint(30, 50)
    while attempts > 0:
        # Select a random cell that is not already empty
        row = randint(0, 8)
        col = randint(0, 8)
        while board[row][col] == 0:
            row = randint(0, 8)
            col = randint(0, 8)
        # Remember its cell value in case we need to put it back
        board[row][col] = 0
        attempts -= 1

def boardGen():
    shuffledBoard(board)
    remover(board)
    return board
