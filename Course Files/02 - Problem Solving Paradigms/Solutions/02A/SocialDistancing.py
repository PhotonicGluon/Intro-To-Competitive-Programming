# INPUT
N, K = [int(x) for x in input().split()]
meals = [int(input()) for _ in range(N)]

# PROCESSING
# First notice that no two hippos can ever be on the same spot - keep only unique meal locations
meals = list(set(meals))

# Now sort the meals in ascending order
meals = sorted(meals)

# We now claim that the optimal solution MUST have the FIRST hippo on the FIRST meal.
# 
# To see why, if we have an optimal solution that DOES NOT use the first meal, we can always move the FIRST
# hippo to the first meal (since the distance from the FIRST meal to the next meal is always bigger than where the
# current meal is to the next meal)
# 
# We can now use a GREEDY algorithm to solve the problem
currLoc = meals[0]  # We can always take the first meal
numMeals = 1        # We took the first meal

for meal in meals[1:]:  # Skip first meal
    # Check if `currLoc + K` is less than (or equal to) the `meal` value (which means that the distancing requirement is met)
    if currLoc + K <= meal:
        # Increment the number of meals taken
        numMeals += 1

        # Update current location
        currLoc = meal

# OUTPUT
print(numMeals)
