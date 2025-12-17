import numpy as np
import re

with open("input_small.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

# 1. Transform input into a 2d array
grid_lines = []
for i, line in enumerate(lines):
    find_number = r"(\d+|[-+*/])"
    matches = re.findall(find_number, line)
    grid_lines.append(matches)


grid = np.array(grid_lines)
print(grid)


# Part 1:
num_rows, num_columns = grid.shape
total_result = 0
for column_idx in range(num_columns):
    operator = grid[-1,column_idx]
    operands = grid[:-1,column_idx]

    assert isinstance(operator, str)
    equation = operator.join(operands)
    result = eval(equation)
    total_result += result

print("total_result:", total_result)


# Part 2:
padded_lines = []
for i, line in enumerate(lines[:-1]):
    check = line


num_rows, num_columns = grid.shape
total_result = 0
for column_idx in range(num_columns):
    operator = grid[-1,column_idx]
    operands = grid[:-1,column_idx]

    # Transform operands into the correct operands
    new_operands = ["" for _ in operands]
    operands = [list(operand) for operand in operands]
    print(operands)
    index = 0

    from itertools import zip_longest

    rows = ["1234", "56"]
    operands = [''.join(c for c in operand if c is not None) for operand in zip_longest(*(reversed(s) for s in operands), fillvalue=None)]
    print("cols", operands)


    assert isinstance(operator, str)
    equation = operator.join(operands)
    result = eval(equation)
    print(str(result) + " = " + equation )
    total_result += result

print("total_result:", total_result)