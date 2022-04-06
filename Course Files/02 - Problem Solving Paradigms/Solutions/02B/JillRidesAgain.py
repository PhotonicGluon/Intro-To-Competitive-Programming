# FUNCTIONS
def max_subarray(numbers):
    """
    Find a contiguous subarray with the largest sum.

    This problem is a modified version of a classic DP problem, known as the Maximum Subarray Problem. The abridged
    problem is as such: find the contiguous subarray within an array such that the sum of its elements is maximised.

    Let's observe a few things about any solution to the problem.
    1. The best sum cannot be negative.
       We can always choose not to take any element for a sum of 0, which is still better than taking negative 
       elements for the sum.

    2. The locally best sum is separated by regions where the sum is zero or negative.
       To see what this means, consider the following array:
            [1, 2, 3, -100, 9, -100, 4, 5, 6, -8, 7, 3]
       Keeping a running total of the sum, we see that for the first three elements the local sum is positive.
       However, upon adding -100, the local sum becomes negative. We thus note that the locally best sum must NOT
       include the -100 as it makes the sum negative, so the locally best sum must come from [1, 2, 3]. We then
       RESET THE LOCAL SUM COUNTER to 0.

       Moving on with element 9, we see the local sum is positive yet again. However adding -100 makes the local
       sum negative. Thus the locally best sum must come from the singleton array [9] and the local sum counter
       is reset to 0.

       Finally, consider the final subarray [4, 5, 6, -8, 7, 3]. Note that at no point in processing this array does
       the local sum counter become negative. Thus we consider this entire subarray as one bloc and the locally best
       sum could have come from here.

    3. The globally best sum (or just best sum) is the maximum of the locally best sums.
       For the subarray [1, 2, 3] its sum is 6; for the subarray [9] its sum is 9; for the subarray [4, 5, 6, -8, 7, 3]
       its sum is 15. Thus the globally best sum is 15, coming from the contiguous subarray [4, 5, 6, -8, 7, 3].

    These three points of information can be used to create the DP solution to the Maximum Subarray Problem. The
    algorithm that is used to solve this problem is known as Kadane's Algorithm, and its implementation is given here.

    The changes that this problem makes from the original Maximum Subarray Problem are:
    1. We want to RETURN the indices of the maximum subarry.
    2. We want to MAXIMISE the length of the maximum subarray.
    
    We address change number 1 first. As described above, we can find and record the indices of the locally best
    subarrays. When we finally compute the final maximum sum, we can update the indices accordingly so that we get the
    maximum subarray.

    Change number 2 is addressed by a special check on whether the current (local) sum equals the best sum and whether
    the current (local) sum has the same starting point as the best sum. If it does, then we can extend the current
    subarray to include the new endpoint.

    Of course the code here has several more optimisations than the algorithm described above. However, the points
    above are the key to understanding Kadane's algorithm (which is what is implemented below).
    """

    best_sum = 0 
    best_start = None  # Starting index of the best subarray
    best_end = None    # Ending index of the best subarray
    current_sum = 0    # Sum of the currently considered subarray

    for current_end, x in enumerate(numbers):
        # Update current sum
        if current_sum <= 0:
            # Start a new sequence at the current element
            current_start = current_end
            current_sum = x
        
        else:
            # Extend the existing sequence with the current element
            current_sum += x

        # Update best sum (if needed)
        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1  # Add 1 to include the actual bus stop number

        elif current_sum == best_sum:
            # Special case; check if the `best_start` is the same as `current_start`
            if best_start == current_start:
                # This is a continuation of the current maximal sum, so include it
                best_end = current_end + 1

    # Return the indices of the best subarray
    return best_start, best_end


# INPUT
s = int(input())
array = [int(input()) for _ in range(s - 1)]  # `s-1` as required by the question

# PROCESSES & OUTPUT
# Apply Kadane's algorithm to the problem at hand
start, end = max_subarray(array)

# Check if there was a best sum
if start is not None and end is not None:
    # Increment both indices by 1 to match the convention in the question, and then output
    print(f"The nicest part of the route is between stops {start+1} and {end+1}")
else:
    # No nice parts
    print("The route has no nice parts")
