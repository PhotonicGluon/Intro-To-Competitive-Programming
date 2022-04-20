from math import sqrt, ceil

while True:
    S, p = [int(x) for x in input().split()]

    if S == 0 and p == 0:
        break

    # Compute the 'ring' that the target square is in
    sqrtOfP = ceil(sqrt(p))

    if sqrtOfP % 2 == 0:
        ring = sqrtOfP // 2 + 1
    else:
        ring = (sqrtOfP + 1) // 2

    # Linear search within the ring to find the spiral tap position
    ringSideLength = 2 * ring - 1

    maxPos = (S + 1) // 2 + (ring - 1)
    minPos = (S + 1) // 2 - (ring - 1)

    X = maxPos
    Y = maxPos
    deltaX = 0  # Change in X per loop
    deltaY = -1  # Change in Y per loop
    currSpiralPos = ringSideLength * ringSideLength

    while True:
        # Check current position
        if currSpiralPos == p:
            print(f"Line = {Y}, column = {X}.")
            break

        # Otherwise update the values of X and Y
        X += deltaX
        Y += deltaY
        currSpiralPos -= 1

        # End-of-loop update/termination conditions
        if X == maxPos and Y == minPos:
            deltaX = -1
            deltaY = 0
        elif X == minPos and Y == minPos:
            deltaX = 0
            deltaY = 1
        elif X == minPos and Y == maxPos:
            deltaX = 1
            deltaY = 0

        if (X == maxPos and Y == maxPos):  # Back to the start
            break
