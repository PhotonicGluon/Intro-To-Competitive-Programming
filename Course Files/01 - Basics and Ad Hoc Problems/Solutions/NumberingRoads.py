caseNo = 1

while True:
    # Get input
    R, N = [int(x) for x in input().split()]
    
    # Check if R = N = 0
    if R == 0 and N == 0:
        break
    
    # Otherwise, compute `(R-1) // N`
    numSuffixes = (R-1) // N  # Minus 1 because if R = N we still don't need to use a suffix
    
    # Check if `numSuffixes` exceeds 26
    if numSuffixes > 26:
        print(f"Case {caseNo}: impossible")
    else:
        print(f"Case {caseNo}: {numSuffixes}")
    
    # Increment the case number
    caseNo += 1