import numpy as np

# Part 1:

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

# 1. Transform input into a 2d array and map '@' to 1 and '.' to 0
for i, line in enumerate(lines):
    line = line.replace('@', '1')
    line = line.replace('.', '0')
    lines[i] = list(line)

grid = np.array(lines, dtype='int32')
print(grid)


def kernel2d(grid, x, y):
    """
    This function counts the number of adjacent rolls
    
    :param grid: 2d numpy array
    :param x: x position in grid to evaluate
    :param y: y position in grid to evaluate
    """

    n_rows, n_cols = grid.shape
    row_start = max(y-1, 0)
    row_end = min(y+2, n_rows)
    col_start = max(x-1, 0)
    col_end = min(x+2, n_cols)

    full_kernel = np.sum(grid[row_start:row_end, col_start:col_end])
    neighbour_kernel = full_kernel - grid[y, x]
    return neighbour_kernel


valid_rolls = 0
def find_valid_rolls(grid):
    """
    This function finds all valid rolls in a grid and returns a new grid where all valid rolls have been removed
    
    :param grid: 2d numpy array 
    """


    valid_rolls = 0
    new_grid = np.copy(grid)
    n_rows, n_cols = grid.shape
    for y in range(n_rows):
        for x in range(n_cols): 
            if grid[y, x] == 1 and kernel2d(grid, x, y) < 4:
                valid_rolls += 1
                new_grid[y, x] = 0
    return valid_rolls, new_grid

valid_rolls, _ = find_valid_rolls(grid)
print("Valid rolls of paper: ", valid_rolls)


# Part 2
final_valid_rolls = 0
while True:
    valid_rolls, grid = find_valid_rolls(grid)

    if valid_rolls == 0:
        break
    final_valid_rolls += valid_rolls 

print("final_valid_rolls: ", final_valid_rolls)
    