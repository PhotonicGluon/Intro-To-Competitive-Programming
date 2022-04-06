# FUNCTIONS
def lowerbound(sorted_arr, val):
    """Finds the SMALLEST index to insert the value `val` so that the elements in `sorted_arr` remain sorted."""
    # Get the length of the array
    n = len(sorted_arr)

    # Perform binary search
    left = 0
    right = n - 1

    while left < right:
        middle = (left + right) // 2

        if sorted_arr[middle] < val:
            left = middle + 1  # Can ignore middle
        else:
            right = middle  # May be on the middle value

    # Return left pointer
    return left


# MAIN CODE
caseNo = 1

while True:
    # Get the value of `N` and `Q`
    N, Q = [int(x) for x in input().split()]

    # Check `N` and `Q`
    if N == 0 and Q == 0:
        break  # End of input

    # Otherwise get numbers and queries
    numbers = [int(input()) for _ in range(N)]
    queries = [int(input()) for _ in range(Q)]

    # Sort the numbers in ascending order
    numbers = sorted(numbers)

    # Process queries
    print(f"CASE# {caseNo}:")
    for query in queries:
        # Get the insertion position of that query
        insertionPos = lowerbound(numbers, query)

        # Check the value at that position
        if numbers[insertionPos] != query:  # Number at the supposed index is not the query number
            # Then the query does not exist inside the list of numbers
            print(f"{query} not found")
        else:
            print(f"{query} found at {insertionPos + 1}")  # Add 1 because it is 1-indexed

    # Increment case number
    caseNo += 1