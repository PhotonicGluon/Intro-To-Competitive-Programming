# IMPORTS
from math import exp, sin, cos, tan


# FUNCTION DEFINIITON
def function(x, p, q, r, s, t, u):
    return p * exp(-x) - q * sin(x) + r * cos(x) - s * tan(x) - t * x * x + u


# MAIN CODE
T = int(input())

for _ in range(T):
    # Split into p, q, r, s, t, u
    p, q, r, s, t, u = [int(x) for x in input().split()]

    # Main processing
    """
    Observe from the constraints given by the question, the function is non-increasing.
    We can use the Bijection method to find a solution.
    """
    left = 0  # Left bound for x
    right = 1  # Right bound for x

    while right - left >= 1e-8:  # While they are still this close
        # Compute midpoint
        m = (left + right) / 2

        # Get value of function at midpoint
        val = function(m, p, q, r, s, t, u)

        # Update pointers appropriately
        if val > 0:
            # The next midpoint needs to be more to the right
            left = m
        
        elif val < 0:
            # The next midpoint needs to be more to the left
            right = m

        else:
            break

    # Compute final estimate for the x-value
    estimate = (left + right) / 2

    # Compute value of the function at this point
    val = function(estimate, p, q, r, s, t, u)

    # Check value
    if abs(val) >= 1e-4:  # Too large
        print("No solution")
    else:  # Within acceptable range
        # print(round(estimate, 4))
        print(f"{estimate:.4f}")
