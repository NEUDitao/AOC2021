
from typing import List, Tuple


lines = open('input', 'r').readlines()

Board = List[List[Tuple[int, bool]]]


def is_bingo(board: Board) -> bool:
    for row in board:
        row_as_bools = [e[1] for e in row]
        if all(row_as_bools):
            return True

    for i in range(len(board[0])):
        acc = True
        for row in board:
            acc = acc and row[i][1]
        if acc:
            return True

    return False


def mark_number(board: Board, num: int) -> Board:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if num == board[i][j][0]:
                board[i][j] = (board[i][j][0], True)

    return board


def calculate_score(board: Board, num: int) -> int:
    acc = 0
    for row in board:
        for col in row:
            if not col[1]:
                acc += col[0]
    return num * acc


drawn_numbers = [int(n) for n in lines[0].split(',')]

og_boards = []
curr_board = []

for line in lines[2:]:
    if line == '\n':
        og_boards.append(curr_board)
        curr_board = []
    else:
        curr_row = [(int(n), False) for n in line.split()]
        curr_board.append(curr_row)

boards = og_boards.copy()

# part 1
for num in drawn_numbers:
    boards = [mark_number(board, num) for board in boards]

    if board := next((board for board in boards if is_bingo(board)), None):
        print('part 1:', calculate_score(board, num))
        break

# part 2
for num in drawn_numbers:
    boards = [mark_number(board, num) for board in boards]

    if len(boards) == 1:
        if is_bingo(boards[0]):
            print('part 2:', calculate_score(boards[0], num))
            break
        else:
            continue

    boards = [board for board in boards if not (is_bingo(board))]
