# Imports
from math import log10, floor

# Precompute
a = [0 for _ in range(10**5+1)]

for i in range(1, 10**5+1):
    a[i] = a[i-1] + log10(i)

# Actual
N = int(input())

for _ in range(N):
    k = int(input())

    # Number of digits in k! = floor(log10(k!)) = floor(log10(k) + log10(k-1) + ... + log10(1))
    print(floor(a[k]) + 1)  # Because even though log10(1) = 0 it still has 1 digit
