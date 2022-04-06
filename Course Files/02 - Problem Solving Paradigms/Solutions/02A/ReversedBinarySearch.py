# FUNCTIONS
def rev_binary_search(arr, target):
    # Define left and right pointers
    l = 0
    r = len(arr) - 1

    # Peform search
    while l <= r:
        # Compute middle
        mid = (l + r) // 2

        # Get middle value
        mid_val = arr[mid]

        # Compare middle value
        if mid_val == target:
            # Stop here and output
            return mid

        elif mid_val < target:
            # Since this is a reversed array, the target has to lie on the left
            r = mid - 1  # Can ignore middle index
        else:
            # Since this is a reversed array, the target has to lie on the right
            l = mid + 1

    # If reached here, means that can't find the element
    return -1


# INPUT
N, K = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]
queries = [int(x) for x in input().split()]

# PROCESSES & OUTPUT
for query in queries:
    print(rev_binary_search(numbers, query) + 1)