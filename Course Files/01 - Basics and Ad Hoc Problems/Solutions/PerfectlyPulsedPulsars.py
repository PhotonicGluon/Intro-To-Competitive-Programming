def gcd(a, b):
    # Euclidean algorithm for computing GCD
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)


N = int(input())
ans = 1  # Current answer

for _ in range(N):
    ans = lcm(ans, int(input()))

print(ans % (10**9 + 7))