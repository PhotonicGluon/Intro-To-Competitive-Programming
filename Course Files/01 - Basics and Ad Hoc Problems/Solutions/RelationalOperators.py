t = int(input())

for _ in range(t):
    # Get the two numbers
    a, b = [int(x) for x in input().split()]
    
    # Compare their relationship
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")