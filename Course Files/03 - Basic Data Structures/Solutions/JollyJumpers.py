# INPUT
t = int(input())

for _ in range(t):
    arr = [int(x) for x in input().split()]
    n = len(arr)

    # PROCESSES
    # Define an auxillary array to keep track of all the differences we see
    differences = [False] * n  # We will ignore index 0

    # Go through the array and calculate differences
    for i in range(n-1):
        diff = abs(arr[i] - arr[i+1])

        if (1 <= diff <= n - 1):
            differences[diff] = True

    # Check if any of the differences is `False`
    isJolly = True
    for i in range(1, n):
        if not differences[i]:   # The absolute difference `i` is not present in the array
            isJolly = False
            break

    # OUTPUT
    if isJolly:
        print("Jolly")
    else:
        print("Not jolly")
