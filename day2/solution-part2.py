import re

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

    # Part 2: IDs are invalid if the have at least 2 times the same order of digits (e.g., 265265265)
    # => Uneven digit lengths are now possible for invalid IDs
    # In this task I want to use regex to perform dynamic pattern matching

    # Iterate over each element in interval al check with multiple pointers if elems are the same
    for id in range(int(start), int(end)+1):
        id_valid = False
        id = str(id)
        
        regex_strings = []
        for idx in range(1, int(len(id) / 2)+1):
            regex_strings.append(f"({id[0:idx]}){{2,}}")

        # Find all substring matches that follow the invalid ID rule
        matches = []
        for regex_string in regex_strings:
            match = re.match(regex_string, id)
            # Found match that is the same as the whole id
            if match and match.group() == id:
                interval_invalid_ids.append(int(id))
                break

        
    total_invalid_ids.append(interval_invalid_ids)
    print("Invalid IDs:", interval_invalid_ids)
print("########################################################")
print("Invalid IDs sum:", sum([sum(interval_ids) for interval_ids in total_invalid_ids]))

