with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

print(lines)

# PART 1
print("#################################################################################")
print("####################### Part 1 ##################################################")
print("#################################################################################")
batteries = []
for bank in lines:
    battery_1 = max(bank[:-1])
    battery_1_idx = bank.find(battery_1)
    print("Battery1:", battery_1, "idx:", battery_1_idx)

    lefover_bank = bank[battery_1_idx + 1:]
    battery_2 = max(lefover_bank)
    battery_2_idx = battery_1_idx + 1 + lefover_bank.find(battery_2)
    print("Battery2:", battery_2, "idx:", battery_2_idx)
    batteries.append(int(battery_1 + battery_2))
print("Total joltage:", sum(batteries))


# PART 2
print("#################################################################################")
print("####################### Part 2 ##################################################")
print("#################################################################################")
batteries = []
for bank in lines:
    bank_batteries = []
    current_battery_idx = 0
    leftover_batteries = [11,10,9,8,7,6,5,4,3,2,1]
    # Take first 11 batteries
    for num_batteries_left in leftover_batteries:
        lefover_bank = bank[current_battery_idx:-num_batteries_left]
        battery = max(lefover_bank)
        battery_idx = lefover_bank.find(battery)

        print("Battery:", battery, "idx:", battery_idx)
        current_battery_idx += battery_idx + 1
        bank_batteries.append(battery)
    # Take last battery
    battery = max(bank[(current_battery_idx):])
    battery_idx = bank.find(battery)
    print("Battery:", battery, "idx:", battery_idx)
    bank_batteries.append(battery)
    print(bank_batteries)
    batteries.append(int("".join(bank_batteries)))
print("Total joltage:", sum(batteries))
    

