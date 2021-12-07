# BRUTE Force: try every possibility and find the minimum cost O(n^2)
# Part 1 completes almost immediately, not worth optimizing. Part 2 takes a
# little longer but still well under a minutes.

positions = [int(x) for x in open('7_input.txt').read().strip().split(',')]

print(max(positions))
minimum_cost = 9999999999
position_for_minimum = -1
# Every possible position
for n in range(max(positions)):
    cost = 0
    for m in range(len(positions)):

        # Solution for a
        # cost += abs(positions[m] - n)

        # Solution for b
        cost += sum(range(abs(positions[m] - n) + 1))

    if cost < minimum_cost:
        position_for_minimum = n
        minimum_cost = cost
print(minimum_cost)




