# DP FUNCTION
def knapsack(item_index, remaining_weight, weights, values, memo_dict):
    # 0. Define needed variables
    n = len(weights)  # Number of items

    # 1. Base Cases
    if remaining_weight == 0:  # If we have no more weight to spare, we cannot take anything
        return 0               # Hence the value of items in our basket is 0
    
    if item_index == n:  # We've reached the end of the list of items; we cannot consider any more items
        return 0         # Hence the value of items in our basket is 0

    if weights[item_index] > remaining_weight:  # The current item's weight is too much
        # Consider the next item
        return knapsack(item_index + 1, remaining_weight, weights, values, memo_dict)

    # 2. Check if we already processed the state already
    key = f"{item_index} {remaining_weight}"  # This uniquely defines this state
    
    if key in memo_dict:  # If already processed
        return memo_dict[key]

    # 3. Process all possible cases
    # Option 1: We take this item
    take_item_value = values[item_index] + knapsack(item_index + 1, remaining_weight - weights[item_index], weights, values, memo_dict)

    # Option 2: We ignore this item
    ignore_item_value = knapsack(item_index + 1, remaining_weight, weights, values, memo_dict)

    # 4. Get optimal solution (Optimal solution achieved when value is maximal)
    max_val = max(take_item_value, ignore_item_value)

    # 5. Update the memoisation dictionary
    memo[key] = max_val

    # 6. Return the answer
    return max_val


# INPUT
S, N = [int(x) for x in input().split()]

V = [None] * N  # Array of values
W = [None] * N  # Array of weights
K = [None] * N  # Array of number of copies of each item

for i in range(N):
    V[i], W[i], K[i] = [int(x) for x in input().split()]

# PROCESSES
# Simply duplicate the weight and value numbers as needed to make it an 0-1 knapsack problem
values = []
weights = []

for i in range(N):
    values += [V[i]] * K[i]  # Add `K[i]` entries of `V[i]` into the values array
    weights += [W[i]] * K[i]  # Add `K[i]` entries of `V[i]` into the values array

# Now use the 0-1 knapsack solution
# (We can do this because the input size is sufficiently small)
memo = {}  # Dictionary to store recursive function calls
answer = knapsack(0, S, weights, values, memo)

# OUTPUT
print(answer)

