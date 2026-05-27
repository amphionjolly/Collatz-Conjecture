import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os
import sys

def get_collatz_3d_data(max_n):
    numbers = []
    steps_list = []
    peaks_list = []
    
    for i in range(1, max_n + 1):
        n = i
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
            
        numbers.append(i)
        steps_list.append(steps)
        peaks_list.append(peak)
        
    return np.array(numbers), np.array(steps_list), np.array(peaks_list)

# Set range (1 to 5000 gives a massive, highly-structured dataset)
#max_range = int(input("Enter the maximum starting number for 3D Collatz analysis"))
if len(sys.argv) > 1:
    max_range = int(sys.argv[1])
else:
    max_range = 5000 # Fallback default

n_val, steps_val, peaks_val = get_collatz_3d_data(max_range)

# Create a combined visualization layout
fig = plt.figure(figsize=(16, 7))

# ----------------------------------------------------
# PLOT 1: 3D Scatter (n vs Steps vs Peak)
# ----------------------------------------------------
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
# Using log10 on peaks because Collatz peaks can shoot up into millions quickly
scatter1 = ax1.scatter(n_val, steps_val, np.log10(peaks_val), 
                       c=steps_val, cmap='plasma', s=2, alpha=0.8)

ax1.set_xlabel('Starting Number (n)')
ax1.set_ylabel('Total Steps to 1')
ax1.set_zlabel('Log10(Max Peak Value)')
ax1.set_title('3D Collatz Landscape', fontsize=12, fontweight='bold')
fig.colorbar(scatter1, ax=ax1, label='Steps', pad=0.1)

# ----------------------------------------------------
# PLOT 2: 2D Color-Mapped Analysis (Clarity View)
# ----------------------------------------------------
ax2 = fig.add_subplot(1, 2, 2)
scatter2 = ax2.scatter(n_val, peaks_val, c=steps_val, 
                       cmap='plasma', s=3, alpha=0.7)

ax2.set_yscale('log')  # Smooths out massive spikes
ax2.set_xlabel('Starting Number (n)')
ax2.set_ylabel('Highest Peak Value (Log Scale)')
ax2.set_title('Peak vs. n (Colored by Path Length)', fontsize=12, fontweight='bold')
fig.colorbar(scatter2, ax=ax2, label='Total Steps')

plt.tight_layout()
folderName=max_range
if not os.path.exists(folderName):
      os.makedirs(f'Confluence Grid 3d/{folderName}')
    
plt.savefig(f"Confluence Grid 3d/{folderName}/collatz_3d_analysis.png", dpi=300)
print("3D and 2D analysis plots generated successfully.")

plt.show()