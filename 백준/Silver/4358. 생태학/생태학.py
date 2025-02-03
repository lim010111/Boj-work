from collections import defaultdict
from sys import stdin


trees = defaultdict(int)
total_trees = 0

for input in stdin.readlines():
    trees[input.rstrip()] += 1
    total_trees += 1

for elem in sorted(trees.items()):
    print(f"{elem[0]} {elem[1] / total_trees * 100:.4f}")