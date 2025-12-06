
# Read file
with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

# Initialize Counter
exact_null_counter = 0
pass_null_counter = 0
current_val = 50

# Iterate over all move instructions
for value in lines:
    direction = value[0]
    degree = int(value[1:])

    print("pass_null_counter:", pass_null_counter, "current_val:", current_val, "move:", value)
    # Right move logic is simple:
    # Use Modulo to end up at correct value (e.g., 56 + R80 => 136 % 100 = 36)
    # Use whole division to count the number of 0 passes. (e.g., 136 // 100 = 1)
    if direction == "R":
        new_val = (current_val + degree) % 100
        pass_null_counter += (current_val + degree) // 100
    
    # Whole division in left move logic has unique characteristics:
    # If new_val ends up at 0, then this should count, but 0 // 100 => 0
    # If starting point is 0, then left move will overcount (e.g., 0 + L10 => -10 // 100 = 1)
    # Should be 0 since the starting 0 was already count before
    else:
        new_val = (current_val - degree) % 100
        
        # Handle case where directly 0
        if new_val == 0:
            pass_null_counter += 1
        # Handle special case for current_val == 0, because 0 - 50 shouldn't add to counter
        if current_val == 0 and new_val != 0:
            pass_null_counter += max(abs((current_val - degree) // 100) - 1, 0)
        else:
            pass_null_counter += abs((current_val - degree) // 100)
    if new_val == 0:
        exact_null_counter += 1
    current_val = new_val
    print("new_val:", new_val, "new_counter:", pass_null_counter)

print("exact_null_counter:", exact_null_counter, "pass_null_counter", pass_null_counter)