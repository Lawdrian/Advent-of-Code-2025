import numpy as np
BEAM = "|"
SPLITTER = "^"
SPACE = "."
START = "S"


with open("input_small.txt", "r") as f:
    lines = f.read().splitlines()
    lines = [list(line) for line in lines]

grid = np.array(lines)

def render_grid(grid):
    print("Grid")
    lines = list(grid)
    for line in lines:
        print("".join(line))


render_grid(grid)

# PART 1
start_col = np.argwhere(grid[0,:] == START)[0][0]
grid[1,start_col] = BEAM
row_idx = 1
n_rows, n_cols = grid.shape
split_counter = 0
while row_idx < n_rows - 1:
    n_rows, n_cols = grid.shape
    print("n_rows", n_rows)
    current_row = grid[row_idx, :]
    # Iterate over every row index and find all beams
    for elem_idx, elem in enumerate(current_row):
        if elem == BEAM:
            if grid[row_idx+1,elem_idx] == SPLITTER:
                split_counter += 1
                grid[row_idx+1,elem_idx-1] = BEAM
                grid[row_idx+1,elem_idx+1] = BEAM
            else:
                grid[row_idx+1,elem_idx] = BEAM
    
    row_idx +=1
    render_grid(grid)
print("Number of splits:", split_counter)

