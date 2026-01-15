import numpy as np


with open("input.txt", "r") as f:
    lines = f.read().splitlines()


# Part 1

### Find four corner points
top_left = (np.inf, np.inf)
bot_left = (np.inf, -np.inf)
top_right = (-np.inf, np.inf)
bot_right = (-np.inf, -np.inf)

n_lines = len(lines)

for line in lines:
    x, y = line.split(',')
    x, y = int(x), int(y)

    # top left
    if x + y <= top_left[0] + top_left[1]:
        top_left = (x, y)
    # bot left
    if y - x >= bot_left[1] - bot_left[0]:
        bot_left = (x, y)
    # top right
    if x - y >= top_right[0] - top_right[1]:
        top_right = (x, y)
    # bot right
    if x + y >= bot_right[0] + bot_right[1]:
        bot_right = (x, y)


print("top_left:", top_left)
print("bot_right:", bot_right)
area1 = (abs(top_left[0] - bot_right[0]) + 1) * (abs(top_left[1] - bot_right[1]) + 1) 
print(area1)
print("top_right:", top_right)
print("bot_left:", bot_left)
area2 = (abs(top_right[0] - bot_left[0]) + 1) * (abs(top_right[1] - bot_left[1]) + 1) 
print(area2)
print("Maximum Area:", max(area1, area2))


"""
max_area = -np.inf
    for j in range(i+1, n_lines):
        x1, y1 = lines[i].split(',')
        x1, y1 = int(x1), int(y1)
        x2, y2 = lines[j].split(',')
        x2, y2 = int(x2), int(y2)

        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1) 
        if area > max_area:
            max_area = area
            print('new area:', area, '1', x1, ',', y1, '2', x2, ',', y2)
        max_area = max(max_area, area)

print(max_area)"""