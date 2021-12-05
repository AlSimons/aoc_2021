"""
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see
any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random,
and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.)
If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time.
It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle
input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are
marked as follows (shown here adjacent to each other to save space):

*****
Note: The "marked" squares are shown on the website as bold.  This doesn't show up here.
***

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
At this point, the third board wins because it has at least one complete row or column of marked numbers
(in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers
on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called

when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final
score be if you choose that board?
"""


def read_draws(f):
    line = f.readline()
    draws = [int(x) for x in line.strip().split(',')]
    return draws


def read_boards(f):
    """
    Some 'splaining.  We're going to store the board data in the form of a dict of lists of tuples.
    The dict keys are the numbers in the board. Each tuple is the location of the number in all
    the boards, (board, row, column).
    :param f: the input file
    :return: boards, position_dict
    """
    position_dict = {}
    board_list = []
    num_boards = -1  # Initialize for zero-based counting
    while True:
        line = f.readline()
        if not line:
            break
        if len(line) == 1:
            # Empty line has only '\n'.
            row_num = -1  # Initialize for zero based counting
            # Create a list for holding the rows
            board = []  # List of rows
            board_list.append(board)
            num_boards += 1
            continue
        row = [int(x) for x in line.strip().split()]
        board_list[num_boards].append(row)
        row_num += 1
        for n in range(5):
            try:
                position_list = position_dict[row[n]]
            except KeyError:
                position_list = []
                position_dict[row[n]] = position_list
            position_list.append((num_boards, row_num, n))  # Double parens: appending a collection
    return board_list, position_dict


def process_draw(draw, position_dict, board_list):
    position_list = position_dict[draw]
    for position in position_list:
        board, row, column = position
        board_list[board][row][column] = -1


def check_for_wins(board_list):  # Returns winning board number
    for n in range(len(board_list)):
        # Check rows
        for r in range(5):
            won = True
            for c in range(5):
                if board_list[n][r][c] != -1:
                    won = False
                    break
            if won:
                return n
        # Check columns
        for c in range(5):
            won = True
            for r in range(5):
                if board_list[n][r][c] != -1:
                    won = False
                    break
            if won:
                return n
    return -1  # Flag for no win yet


def score(board_list, winning_board, winning_draw):
    board = board_list[winning_board]
    unfilled_squares_total = 0
    for row in range(5):
        for column in range(5):
            cell_value = board[row][column]
            if cell_value != -1:
                unfilled_squares_total += cell_value
    return unfilled_squares_total * winning_draw


def main():
    with open('4/input.txt') as f:
        draws = read_draws(f)
        board_list, position_dict = read_boards(f)
    for draw in draws:
        process_draw(draw, position_dict, board_list)
        winning_board = check_for_wins(board_list)
        if winning_board != -1:  # Flag for no win yet
            break
    print(score(board_list, winning_board, draw))


if __name__ == '__main__':
    main()
