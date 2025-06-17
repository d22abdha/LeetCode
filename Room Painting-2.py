# Read the first line of input
first_line = input().split()
number_of_cans = int(first_line[0])
number_of_needs = int(first_line[1])

# Read can sizes
can_list = []
for x in range(number_of_cans):
    cans = int(input())
    can_list.append(cans)

# Sort can sizes to find the smallest suitable one faster
can_list.sort()

# Read paint needs
can_needs_list = []
for x in range(number_of_needs):
    can_needs = int(input())
    can_needs_list.append(can_needs)

# Calculate total waste
total_waste = 0

for can_needs in can_needs_list:
    for i, cans in enumerate(can_list):
        if cans >= can_needs:
            total_waste += (cans - can_needs)
            break
print(total_waste)

