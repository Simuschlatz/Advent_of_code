import numpy as np

with open("input.txt", "r") as file:
    trees = np.array([list(map(int, [*line.rstrip()])) for line in file.readlines()])
num_rows, num_cols = len(trees), len(trees[0])

def detect_visibles(trees, visibles, transposed=False):
    ranges = [range(1, num_cols - 1), range(num_cols-2, 0, -1)]
    for i, row in enumerate(trees[1:-1], start=1):
        for direction in range(2):
            max_height = row[-direction] # index 0 or -1
            for tree in ranges[direction]:
                if row[tree] > max_height:
                    max_height = row[tree]
                    if transposed: visibles[tree][i] = True
                    else: visibles[i][tree] = True

def part_one():
    visibles = np.zeros(shape=(num_rows, num_cols), dtype=np.bool8)
    detect_visibles(trees, visibles)
    detect_visibles(trees.T, visibles, transposed=True) # doing the same thing, now rows are cols and cols are rows
    print(f"Part one: {np.sum(visibles) + 392}") # Didn't mark outer trees as visible, so add them to the end result

def part_two():
    dd = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dists = [None] * 4
    max_score = 0
    for i, row in enumerate(trees[1:-1], start=1):
        dists[0], dists[1] = i, num_rows - 1 - i
        for j, height in enumerate(row[1:-1], start=1):
            score = 1
            dists[2], dists[3] = j, num_cols - 1 - j
            for (di, dj), d in zip(dd, dists):
                for step in range(1, d + 1):
                    ii, jj = i + step * di, j + step * dj
                    tree = trees[ii][jj]
                    if tree >= height: 
                        score *= step
                        break
                else: score *= d # neveer in my life would I've thought I'd use for else
            max_score = max(score, max_score)
    print(f"Part two: {max_score}")
                
part_one()
part_two()

