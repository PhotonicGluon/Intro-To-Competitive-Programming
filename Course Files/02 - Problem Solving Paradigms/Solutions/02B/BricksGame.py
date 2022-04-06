# FUNCTIONS
def solution(n, arr):
    """
    Let's start simple: considering the base cases.
    - When there is one brick left, we should obviously take the only brick left.
    - When there are two bricks left, we should take both bricks.
    - When there are three bricks left, we should take all three bricks.

    The intresting part starts when there are 4 bricks left.

    Suppose we are left with the bricks
        [1, 2, 3, 4]
    and it is our turn to make a move. What is our optimal play? Well, we can either take one brick, two bricks, or
    three bricks.
        - If we take 1 brick, opponent is left with [2, 3, 4] which he will obviously take all of them. We score 1.
        - If we take 2 bricks, opponent is left with [3, 4] which he will obviously take all of them. We score 
          1 + 2 = 3.
        - If we take 3 bricks, opponent is left with [4] which he will obviously take. We score 1 + 2 + 3 = 6.

    Let's analyse our thought process. What are we considering when we are making this argument?

    For starters, we are assuming that the opponent is making optimal play. But optimal play is also what WE are
    aiming for. Thus we can conclude that the opponent is using the SAME STRATEGY as we are.

    Now let's finally introduce some DP terminology. Define the DP array as follows:
        dp[-i] = (optimal score, number of bricks taken in this move)
    where `dp[-i]` represents that tuple in the case where there are `i` bricks left (hence the minus sign).

    Back to our problem. Suppose we start with $k$ bricks remaining and we take one brick. What will our opponent's
    move be? Or rather, what is the *state* that our opponent will be in? Well, if we take one brick, our opponent will
    be left with $k - 1$ bricks, so the state is `dp[-(k-1)] = dp[-k + 1]`. Now our opponent's move will be
    `dp[-k + 1][1]` (since the second value of the DP state is the number of bricks that we should take) and we'll be
    left with `(k-1) - dp[-k + 1][1]` bricks. The state that WE need to play is now `dp[-((k-1) - dp[-k + 1][1])]`
    which simplifies to `dp[-k + dp[-k + 1][1] + 1]`. The score we would attain in this case would thus be
        `dp[-k + dp[-k + 1][1] + 1][0] + arr[-k]`
    where `arr` contains the bricks' scores.

    Repeating the above argument for the other two types of moves (i.e. taking 2 bricks or taking 3 bricks) yields
    the score in all three cases:
        Taking 1 brick score:       dp[-k + dp[-k + 1][1] + 1][0] + arr[-k]
        Taking 2 bricks' score:     dp[-k + dp[-k + 2][1] + 2][0] + arr[-k] + arr[-k + 1]
        Taking 3 bricks' score:     dp[-k + dp[-k + 3][1] + 3][0] + arr[-k] + arr[-k + 1] + arr[-k + 2]
    The optimal score for the state when we have `k` bricks left is thus the MAXIMUM of these three scores. The number
    of bricks taken naturally follows.
    """

    # Create the table
    dp = [(0, 0) for _ in range(n + 1)]  # First element is the max score, second element is number of bricks to take
    
    # Set base cases
    dp[-1] = (arr[-1], 1)                      # When there is 1 brick left, it is optimal to just take that brick
    dp[-2] = (arr[-1] + arr[-2], 2)            # When there are 2 bricks left, it is optimal to just take both bricks
    dp[-3] = (arr[-1] + arr[-2] + arr[-3], 3)  # When there are 3 bricks left, it is optimal to just take the three bricks
    
    # Process the rest of the cases
    for bricks_left in range(4, n + 1):
        # Consider all possible moves that we can take and the maximum score in each case
        take1brick  = dp[-bricks_left + dp[-bricks_left + 1][1] + 1][0] + arr[-bricks_left]
        take2bricks = dp[-bricks_left + dp[-bricks_left + 2][1] + 2][0] + arr[-bricks_left] + arr[-(bricks_left - 1)]
        take3bricks = dp[-bricks_left + dp[-bricks_left + 3][1] + 3][0] + arr[-bricks_left] + arr[-(bricks_left - 1)] + \
                      arr[-(bricks_left - 2)]
        
        # Determine the best option
        options = [take1brick, take2bricks, take3bricks]
        best_option = max(options)
        
        # Update the DP table
        dp[-bricks_left] = (best_option, options.index(best_option) + 1)  # 2nd element is the number of bricks taken
    
    # Return the score for the initial case of having all the bricks
    return dp[-n][0]

# INPUT
t = int(input())

for _ in range(t):
    n = int(input())
    A = [int(x) for x in input().split()]

    # PROCESSES
    # Solve the problem using the function
    answer = solution(n, A)

    # OUTPUT
    print(answer)
