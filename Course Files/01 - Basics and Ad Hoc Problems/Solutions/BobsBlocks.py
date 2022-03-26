# Input
N = int(input())

# Compute height and volume
height = 0
volume = 0
for i in range(1, N + 1):
    height += i
    volume += i*i*i  # Same as i cubed

# Output
print(height, volume)