# INPUT
N, m = [int(x) for x in input().split()]
schools = [int(input()) for _ in range(m)]

# PROCESSES
# Sort the schools by the number of lunchboxes desired
schools = sorted(schools)

# Greedily get as many schools as possible, starting with the schools that require the least number of boxes first
total = 0
index = 0
while total <= N and index < m:
    if total + schools[index] > N:
        break
    else:
        total += schools[index]

    index += 1

# OUTPUT
# The index is the number of schools that we have taken up
print(index)
