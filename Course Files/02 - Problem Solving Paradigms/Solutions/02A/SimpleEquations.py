# INPUT
N = int(input())

for _ in range(N):
    A, B, C = [int(x) for x in input().split()]

    # PROCESSING & OUTPUT
    """
    Observe the third equation's condition:
    x^2 + y^2 + z^2 = C

    Since it is given that 1 <= C <= 10^3, we can conclude that -32 < -10^{3/2} <= x <= 10^(3/2) < 32. The logic is:
    assume that y = 1 and z = 2 (need to be distinct). Then for x^2 + 5 = C^2 <= 10^3, we must have -10^(3/2) <= x <= 10^(3/2).
    This argument applies also to y and z, which means we have a good bound on x, y, and z:

    -32 <= x, y, z <= 32

    This means that we only have 65 * 65 * 65 = 274,625 integers to check. Further since all three integers are
    distinct we can quickly short-circuit any case where x = y or y = z or x = z. For N = 20 this means that, in the
    worst case we only have to check 5,492,500 cases - definitely solvable.
    """

    # Solution
    sol = False
    for x in range(-32, 33):          # This guarrentees smallest x first
        for y in range(-32, 33):      # This guarrentees smallest y first
            for z in range(-32, 33):  # This guarrentees smallest z first
                # Check if they are equal
                if (x == y) or (y == z) or (x == z):
                    continue  # Skip this

                # Otherwise, check if the three conditions are met
                if (x*x + y*y + z*z) == C and (x * y * z == B) and (x + y + z == A):  # Start with most restrictive condition first
                    print(x, y, z)
                    sol = True
                    break

            if sol:
                break

        if sol:
            break

    if not sol:
        print("No solution.")

