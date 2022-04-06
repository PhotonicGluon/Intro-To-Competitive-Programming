# IMPORTS
from itertools import product

# INPUT
L = int(input())
N = int(input())
bars = [int(x) for x in input().split()]

# PROCESSES & OUTPUT
# Since 2^15 = 32768 < 10^8, it is definitely feasible to do a complete search
allPossible = product([0, 1], repeat=N)
isFound = False

for possible in allPossible:
    # Sum according to the specified bars taken
    sum_ = 0

    for i, takeOrNot in enumerate(possible):
        sum_ += takeOrNot * bars[i]

    # Check if the sum equals the target length
    if sum_ == L:
        print("YES")
        isFound = True
        break

if not isFound:
    print("NO")
