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


# PART 2
with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    lines = [list(line) for line in lines]

grid = np.array(lines)

start_col = np.argwhere(grid[0,:] == START)[0][0]
n_rows, n_cols = grid.shape

# Track how many timelines have a beam at each column
beams_at_col = [0] * n_cols
beams_at_col[start_col] = 1

# Process each row downward
for row_idx in range(1, n_rows - 1):
    next_beams_at_col = [0] * n_cols
    for elem_idx in range(n_cols):
        if beams_at_col[elem_idx] > 0:
            below = grid[row_idx + 1, elem_idx]
            if below == SPLITTER:
                # 2 new timelines
                next_beams_at_col[elem_idx - 1] += beams_at_col[elem_idx]
                next_beams_at_col[elem_idx + 1] += beams_at_col[elem_idx]
            else:
                # Continue down
                next_beams_at_col[elem_idx] += beams_at_col[elem_idx]
    beams_at_col = next_beams_at_col

total_timelines = sum(beams_at_col)
print("Total timelines:", total_timelines)