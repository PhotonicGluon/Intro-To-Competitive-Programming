while True:
    N = int(input())

    if N == 0:
        break

    while True:
        arrangement = [int(x) for x in input().split()]

        if len(arrangement) == 1 and arrangement[0] == 0:
            break

        # Attempt to create the desired arrangement by popping any matching coaches immediately
        coachNo = 1
        index = 0  # Index of the coach in the arrangement
        station = []  # Essentially a stack

        while coachNo <= N + 1 and index < N:  # Use N + 1 to account for case when it is only possible at the end
            # Check if can pop from station
            if len(station) != 0 and station[-1] == arrangement[index]:
                station.pop()  # Remove latest coach
                index += 1
            else:
                station.append(coachNo)
                coachNo += 1

        # If there are still coaches at the station it is not possible
        if len(station) != 0:
            print("No")
        else:
            print("Yes")

    print()
