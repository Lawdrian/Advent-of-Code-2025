# Load input
with open ('input.txt', 'r') as file:
    lines = file.read()


intervalls, ingredients = lines.split('\n\n')
intervalls = intervalls.split()
ingredients = ingredients.split()



### Store valid ids in a set => Not performant
"""
# Create set of valid ingredient ids
for intervall in intervalls:
    start, end = intervall.split('-')
    

    for id in range(int(start), int(end)+1):
        valid_ids.add(id)
"""

# Try another approach => Create efficient list of intervalls
for i, intervall in enumerate(intervalls):
    start, end = intervall.split('-')
    intervalls[i] = [int(start), int(end)]


# Create efficient intervalls
sorted_intervalls = sorted(intervalls, key=lambda intervall: intervall[0])
efficient_intervalls = [sorted_intervalls[0]]
for i in range(1, len(sorted_intervalls)):
    intervall_idx = len(efficient_intervalls) - 1
    # 1. next intervall longer ending
    if efficient_intervalls[intervall_idx][1] >= sorted_intervalls[i][0] and efficient_intervalls[intervall_idx][1] < sorted_intervalls[i][1]:
        efficient_intervalls[intervall_idx][1] = sorted_intervalls[i][1]
    # 2. next intervall starts after current intervall ends
    elif efficient_intervalls[intervall_idx][1] < sorted_intervalls[i][0]:
        efficient_intervalls.append(sorted_intervalls[i])


# Part 1
# Iterate through ingredient list and count valid ingredients
num_valid = 0

ingredients = sorted(ingredients)
for ingredient in ingredients:
    ingredient = int(ingredient)
    intervall_idx = 0
    while intervall_idx < len(efficient_intervalls):
        if ingredient <= efficient_intervalls[intervall_idx][1] and ingredient >= efficient_intervalls[intervall_idx][0]:
            num_valid += 1
            break
        intervall_idx += 1
    
print("num valid ingredients: ", num_valid)


# Part 2
# Count number of elements between intervalls
num_valid_ids = 0
for intervall in efficient_intervalls:
    num_valid_ids += intervall[1] - intervall[0] + 1

print("num valid ids: ", num_valid_ids)
