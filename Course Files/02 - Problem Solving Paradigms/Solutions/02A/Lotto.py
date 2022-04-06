# INPUT
k = int(input())
S = [int(x) for x in input().split()]

# PROCESSES & OUTPUT
# Simply generate all possible cases through the use of complete search (although this uses SIX for loops)
for a in range(k - 5):
    for b in range(a + 1, k - 4):
        for c in range(b + 1, k - 3):
            for d in range(c + 1, k - 2):
                for e in range(d + 1, k - 1):
                    for f in range(e + 1, k):
                        print(f"{S[a]} {S[b]} {S[c]} {S[d]} {S[e]} {S[f]}")
