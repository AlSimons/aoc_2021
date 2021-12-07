# BRUTE Force: try every possibility and find the minimum cost O(n^2)
# Part 1 completes almost immediately, not worth optimizing. Part 2 takes a
# little longer but still well under a minutes.

positions = [int(x) for x in open('7_input.txt').read().strip().split(',')]

minimum_cost_a = 9999999999
minimum_cost_b = 9999999999
# Every possible position
for n in range(max(positions)):
    cost_a = 0
    cost_b = 0
    for m in range(len(positions)):
        cost_a += abs(positions[m] - n)
        cost_b += sum(range(abs(positions[m] - n) + 1))

    if cost_a < minimum_cost_a:
        minimum_cost_a = cost_a
    if cost_b < minimum_cost_b:
        minimum_cost_b = cost_b
print(f"Part A: {minimum_cost_a}\nPart B: {minimum_cost_b}")




