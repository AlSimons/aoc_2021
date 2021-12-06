"""
--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents
constantly produce large, opaque clouds, so it would be best to avoid them if
possible.

They tend to form in lines; the submarine helpfully produces a list of nearby
lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2
where x1,y1 are the coordinates of one end the line segment and x2,y2 are
the coordinates of the other end. These line segments include the points at
both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either
x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the
following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is
9,9. Each position is shown as the number of lines which cover that point
or . if no line covers that point. The top-left pair of 1s, for example,
comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping
lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of
points where at least two lines overlap. In the above example, this is
anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at
least two lines overlap?

For part 2, also consider 45 deg. diagonals.
"""
import timer
t = timer.Timer()

# names for the collection indices.
x = 0
y = 1


def compute_points(start, end, iteration):
    """
    Given two points, compute all the points between, inclusive. For part 1.
    consider only rows and columns. For part 2, also include 45 deg. diagonals
    :param start: A tuple of coordinates, (x, y)
    :param end: Ditto
    :param iteration: Whether we're doing part 1 or 2
    :return: a list of tuples lying on any column or row common to the start
    and finish.  An empty list if no common row, column or (in part 2) diagonal.
    """
    if start[x] == end[x]:
        return compute_col_points(start, end)
    elif start[y] == end[y]:
        return compute_row_points(start, end)
    # Check for 45 deg. diagonals
    elif iteration == 2 and abs(start[x] - end[x]) == abs(start[y] - end[y]):
        return compute_diagonal_points(start, end)
    return []


def compute_col_points(start, end) -> list:
    x_coord = start[x]
    # Normalize the coordinates so we can work from low to high.
    sy, ey = start[y], end[y]
    if sy > ey:
        sy, ey = ey, sy

    points = []
    for y_coord in range(sy, ey + 1):
        points.append((x_coord, y_coord))
    return points


def compute_row_points(start, end) -> list:
    y_coord = start[y]
    # Normalize the coordinates so we can work from low to high.
    sx, ex = start[x], end[x]
    if sx > ex:
        sx, ex = ex, sx

    points = []
    for x_coord in range(sx, ex + 1):
        points.append((x_coord, y_coord))
    return points


def al_compute_diagonal_points(start, end):
    t.start()
    sx, sy = start
    ex, ey = end
    # normalize both points to increasing x axis order
    # If positive slope, ey will be > sy, if negative, sy > ey
    if sx > ex:
        sx, ex = ex, sx
        sy, ey = ey, sy
    # We know that the distance between both starts and ends is the same here.
    distance = ex - sx
    points = []
    for n in range(distance + 1):  # Plus 1 due to closed interval
        x_coord = sx + n
        y_coord = sy + n if sy < ey else sy - n
        points.append((x_coord, y_coord))
    t.stop()
    return points


def compute_diagonal_points(start, end):
    t.start()
    x_a = start[x]
    x_b = end[x]
    y_a = start[y]
    y_b = end[y]
    points = []
    x_range = range(x_a, x_b + (1 if x_a < x_b else -1),
                    1 if x_a < x_b else -1)
    y_range = range(y_a, y_b + (1 if y_a < y_b else -1),
                    1 if y_a < y_b else -1)
    for i in range(len(x_range)):
        points.append((x_range[i], y_range[i]))
    t.stop()
    return points


def parse_line(line):
    text_coords = line.split(' -> ')
    start = text_coords[0].split(',')
    start = (int(start[x]), int(start[y]))
    end = text_coords[1].split(',')
    end = (int(end[x]), int(end[y]))
    return start, end


points_dict = {}


def mark_points(points_list):
    for point in points_list:
        try:
            points_dict[point] += 1
        except KeyError:
            points_dict[point] = 1


def check():
    hotspots = 0
    for point_key in points_dict.keys():
        if points_dict[point_key] > 1:
            hotspots += 1
    return hotspots


def main():
    global points_dict
    for iteration in [1, 2]:
        # Have to initialize our point tracker for each iteration
        points_dict = {}
        for line in open('5_input.txt'):
            start, end = parse_line(line.strip())
            # Get a list of all the points affected by this pair of points.
            points_list = compute_points(start, end, iteration)
            if points_list:
                mark_points(points_list)
        print(check())
        print(t)
        t.reset()


if __name__ == '__main__':
    main()
