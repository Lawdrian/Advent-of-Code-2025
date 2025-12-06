# Read file
with open("day2/input.txt", "r") as f:
    text = f.read()
    intervals = text.split(",")

total_invalid_ids = []
for interval in intervals:
    interval_invalid_ids = []
    start, end = interval.split("-")
    print("########################################################")
    print("Interval:", interval)

    # Part 1: IDs are invalid if the have exactly 2 times the same order of digits (e.g., 265265)
    # Iterate over each element in interval al check with 2 pointers if elems are the same
    for id in range(int(start), int(end)+1):
        id_valid = False
        id = str(id)
        # Digits with uneven lengths are all valid
        if len(id) % 2 == 1:
            continue 
        
        first_idx, second_idx = 0, int(len(id) / 2)
        while second_idx < len(id):
            if id[first_idx] != id[second_idx]:
                id_valid = True
                break
            first_idx += 1
            second_idx += 1
        if not id_valid:
            interval_invalid_ids.append(int(id))
    total_invalid_ids.append(interval_invalid_ids)
    print("Invalid IDs:", interval_invalid_ids)
print("########################################################")
print("Invalid IDs sum:", sum([sum(interval_ids) for interval_ids in total_invalid_ids]))

