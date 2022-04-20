while True:
    # INPUT
    N, M = [int(x) for x in input().split()]

    if N == 0 and M == 0:
        break

    # Store the CDs into sets
    jack = set([input() for _ in range(N)])
    jill = set([input() for _ in range(M)])

    # PROCESSING
    # We can find the common CD catalogues by using the set intersection
    common = jack.intersection(jill)

    # OUTPUT
    print(len(common))  # Number of common CDs
