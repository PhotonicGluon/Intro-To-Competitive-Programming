caseNo = 1

while True:
    t = int(input())

    if t == 0:    # Halt if the `t` value is 0
        break

    # Process the teams
    member_to_team = {}  # Use a dictionary to keep track of a member's team
    for team in range(t):
        teamMembers = [int(x) for x in input().split()][1:]
        for member in teamMembers:
            member_to_team[member] = team 

    # Process the queue requests
    print(f"Scenario #{caseNo}")
    teamQueue = {}  # Use a dictionary as it preserves insertion order

    while True:
        command = input()

        if command == "STOP":
            break
        elif command == "DEQUEUE":
            # Get the key of the earliest inserted team
            key = list(teamQueue.keys())[0]

            # Remove first element of that team
            print(teamQueue[key].pop(0))

            # Check if that list is empty
            if len(teamQueue[key]) == 0:
                # Delete this key
                del teamQueue[key]

        else:  # Command is ENQUEUE
            # Get the element to enqueue
            elem = int(command.split()[1])

            # Get the team that this element belongs to
            teamNo = member_to_team[elem]

            # Add to team queue
            if teamNo in teamQueue:
                teamQueue[teamNo].append(elem)
            else:
                teamQueue[teamNo] = [elem]

    # Increment case number
    caseNo += 1
    print()
