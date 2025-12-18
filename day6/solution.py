import numpy as np
import re

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

# 1. Transform input into a 2d array
grid_lines = []
for i, line in enumerate(lines):
    find_number = r"(\d+|[-+*/])"
    matches = re.findall(find_number, line)
    grid_lines.append(matches)

grid = np.array(grid_lines)

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

print("part1 total result:", total_result)


# Part 2:
with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    results = []
    i = 0
    while i < len(lines[0]):
        operator = lines[-1][i]
        operands = []
        elems = [line[i] for line in lines[:-1]]
        while any([True for elem in elems if elem != " "]):
            operands.append("".join(elems))
            # Check next number in current batch
            if i < len(lines[0])-1:
                i += 1
                elems = [line[i] for line in lines[:-1]]
            elif i == len(lines[0]) - 1:
                break
        i += 1
        # Caclulate number
        operands = [operand.strip() for operand in operands]
        equation = operator.join(operands)
        result = eval(equation)
        #print(f"{result} = {equation}")
        results.append(result)

total_result = sum([int(result) for result in results])
print("part2 total result:", total_result )