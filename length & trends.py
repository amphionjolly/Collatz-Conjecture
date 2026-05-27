import matplotlib.pyplot as plt
import sys

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 20 # Fallback default

def collatz_metrics(n):
    steps = 0
    peak = n
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n > peak:
            peak = n
        steps += 1
    return steps, peak

# Run for first 1000 numbers
numbers = list(range(1, 21))
results = [collatz_metrics(n) for n in numbers]
steps, peaks = zip(*results)

# Plotting Stopping Times
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(numbers, steps, s=2, alpha=0.6, color='crimson')
plt.title("Starting Number vs Total Steps")
plt.xlabel("Starting Number (n)")
plt.ylabel("Steps to reach 1")

# Plotting Peaks
plt.subplot(1, 2, 2)
plt.scatter(numbers, peaks, s=2, alpha=0.6, color='blue')
plt.yscale('log')  # Log scale handles massive peaks smoothly
plt.title("Starting Number vs Highest Peak (Log Scale)")
plt.xlabel("Starting Number (n)")
plt.ylabel("Highest Value Reached")

plt.tight_layout()
plt.show()