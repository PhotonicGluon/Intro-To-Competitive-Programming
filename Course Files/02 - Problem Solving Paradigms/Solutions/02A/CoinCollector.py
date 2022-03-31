# INPUT
T = int(input())

for _ in range(T):
    n = int(input())
    coins = [int(x) for x in input().split()]  # Note that we know this is strictly increasing

    # PROCESSING
    # Observe that we always want to take the coin valued at 1
    currSum = 1
    numCoins = 1
    for i in range(1, n - 1):
        if currSum + coins[i] < coins[i+1]:  # If the total value of taking these two coins is less than the next coin
            # Then we can take this coin without worry
            numCoins += 1
            currSum += coins[i]

    # Note we can also always take the last coin
    if n != 1:  # There is more than one coin
        numCoins += 1

    # OUTPUT
    print(numCoins)
