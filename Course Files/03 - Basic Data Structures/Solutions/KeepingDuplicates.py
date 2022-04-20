# INPUT
counts = {}  # Dictionary storing number of occurances
while True:
    # Read in the element
    elem = input()

    # Check if the element is "0"
    if elem == "0":
        break

    # Otherwise, increment the count of that element
    if elem not in counts:
        counts[elem] = 1
    else:
        counts[elem] += 1

# PROCESSING AND OUTPUT
haveDuplicates = False

for key, value in counts.items():  # This does it in insertion order
    if value >= 2:  # Have duplicates
        haveDuplicates = True
        print(key, value)

if not haveDuplicates:
    print("No duplicates")
