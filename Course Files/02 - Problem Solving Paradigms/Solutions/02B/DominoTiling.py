# INPUT
N = int(input())

# PROCESSES & OUTPUT
# Base cases
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    """
    We observe that the recurrance relation to obtain the next solution is as follows:
        a_{n+2} = a_{n+1} + a_n
    where a_i represents the number of ways that Accifibon can tile a 2 x i chessboard.

    Notice also that a_1 = 1 and a_2 = 2. We thus established a recurrance relation.

    The intesting thing about this relation is that we can reach the solution WITHOUT using any recursion; we can use
    an iterative approach to get the required answer.
    """

    a = 1
    b = 2

    for _ in range(N - 2):
        temp = a
        a = b
        b = temp + b

    print(b % (10**9 + 7))  # We need to give the answer modulo 10^9 + 7
