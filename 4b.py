"""
(See 4a, for the first part of the the description...)

On the other hand, it might be wise to try a different strategy: let the
giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so
rather than waste time counting its arms, the safe thing to do is to figure
out which board will win last and choose that one. That way, no matter
which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens
after 13 is eventually called and its middle column is completely marked.
If you were to keep playing until this point, the second board would have a
sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final
score be?
"""

# This is mostly 4a, with a slight termination


def read_draws(f):
    line = f.readline()
    draws = [int(x) for x in line.strip().split(',')]
    return draws


def read_boards(f):
    """
    Some 'splaining.  We're going to store the board data in the form of a
    dict of lists of tuples.
    The dict keys are the numbers in the board. Each tuple is the location
    of the number in all the boards, (board, row, column).
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
        try:
            board_list[board][row][column] = -1
        except IndexError:
            # Boards disappear when they win.
            pass


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


def score(board, winning_draw):
    unfilled_squares_total = 0
    for row in range(5):
        for column in range(5):
            cell_value = board[row][column]
            if cell_value != -1:
                unfilled_squares_total += cell_value
    return unfilled_squares_total * winning_draw


def main():
    with open('4_input.txt') as f:
        draws = read_draws(f)
        board_list, position_dict = read_boards(f)
    num_winners = 0
    for draw in draws:
        process_draw(draw, position_dict, board_list)
        winning_board = check_for_wins(board_list)
        if winning_board != -1:  # Flag for no win yet
            last_winning_board = board_list.pop(winning_board)
            last_winning_draw = draw
            continue
    print(score(last_winning_board, last_winning_draw))


if __name__ == '__main__':
    main()
