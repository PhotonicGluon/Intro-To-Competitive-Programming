# INPUT
N = int(input())
A = [int(input()) for _ in range(N)]

# PROCESSES
"""
Critical observation:
    To reach a value $V$, we must have come from a value SMALLER than $V$ AND that is before it.

Assuming that ALL values before $V$ have an optimal solution, we can find the optimal solution for $V$.

Define the DP table as `dp[i]`, where `i` is the index of the element. The value of `dp[i]` represents the length of
the longest rising subsequence that ENDS at index `i`.

The base case is `dp[0] = 1` because if we end at index 0, the optimal solution is to take the first element.

The transition is as follows:
    dp[i] = (Maximum of `dp[j]` for all `j < i` and where `array[j] < array[i]`) + 1
As stated above, we must have come from an element that is SMALLER than the current element, hence the condition of
`array[j] < array[i]`. We find the maximum of all `dp[j]` (i.e. longest rising length) in order to find the maximum
for this current element. We add 1 to the maximum as we are including the current element.
"""

dp = [None] * N  # Make a list with `N` spaces so that we can store all of the states

dp[0] = 1  # The base case

for i in range(1, N):  # We don't have to process the case where `i = 0` because that's the base case
    curr_max = 1  # Set to 1 initially, representing the case where we JUST take this element itself

    for j in range(i):  # Up to but not including i
        # Check if the current element is bigger than this element
        if A[i] > A[j]:
            # Get the DP solution for that element
            possible_sol = dp[j] + 1  # Remember to add 1 for the current element!

            # Update maximum as necessary
            if possible_sol > curr_max:
                curr_max = possible_sol

    # Update DP table
    dp[i] = curr_max

# Now we have computed all longest maximal rising subsequece lengths that end at every index, we find the longest such
# subsequence by using the `max` function
answer = max(dp)

# OUTPUT
print(answer)
