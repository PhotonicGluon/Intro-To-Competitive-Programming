# INPUT
N = int(input())

# FUNCTIONS
def prime_buzz(n): 
    # Finding Primes
    prime = [True for i in range(n + 1)] 
    p = 2

    while (p * p <= n): 
        # If `prime[p]` is not changed, then it is a prime 
        if (prime[p] == True): 
            # Update all multiples of `p` 
            for i in range(p * p, n + 1, p): 
                prime[i] = False

        # Increment current number by 1
        p += 1

    # Get all the primes
    primes = set()
    for i in range(2, n + 1):
        if prime[i]:
            primes.add(i)

    # Get all the buzzes & primebuzzes
    buzzes = set()
    primebuzzes = set()

    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if prime[i]:
                primebuzzes.add(i)
                primes.discard(i)
            else:
                buzzes.add(i)

    # Return K
    return len(primes) * len(buzzes) * len(primebuzzes)

# COMPUTATION & OUTPUT
print(prime_buzz(N))