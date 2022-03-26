# IMPORTS
from math import inf

# INPUT
N = int(input())
integers = [int(input()) for _ in range(N)]


# FUNCTIONS
def two_sum(arr, target):
    # Define variables
    doubles = set()  # Set of all solutions
    n = len(arr)

    # Store all possible values
    allValues = {}  # We use a dictionary as it has efficient key checking

    for i in range(n):
        # Compute the complement
        complement = target - arr[i]

        # Check if the complement exists
        if complement in allValues:
            doubles.add(tuple(sorted([arr[i], complement])))  # Shockingly this sorting is O(1)
            
        # Update the all values dictionary
        allValues[arr[i]] = arr[i]

    # Return all doubles
    return doubles


# COMPUTATIONS
# Get all the possible sets of positions
doubles = two_sum(integers, 2345)

# Get the maximum product of all the integers at those positions
maxProduct = -inf
maxSet = None

for double in doubles:
    product = 1
    for val in double:
        product *= val

    maxProduct = max(maxProduct, product)

# OUTPUT
print(maxProduct)