import matplotlib.pyplot as plt
import numpy as np
import os
import sys

def get_parity_matrix(max_n, max_steps=30):
    matrix = np.zeros((max_n, max_steps))
    for i in range(1, max_n + 1):
        n = i
        step = 0
        while n > 1 and step < max_steps:
            if n % 2 == 0:
                matrix[i-1, step] = 0
                n = n // 2
            else:
                matrix[i-1, step] = 1
                n = 3 * n + 1
            step += 1
    return matrix

if len(sys.argv) > 1:
    max_n = int(sys.argv[1])
else:
    max_n = 20

matrix = get_parity_matrix(max_n)

plt.figure(figsize=(10, 8))
plt.imshow(matrix, cmap='binary', aspect='auto', origin='upper')
plt.colorbar(ticks=[0, 1], label='0 = Even (White) | 1 = Odd (Black)')
plt.xlabel('Step Number')
plt.ylabel('Starting Number (n)')
plt.title(f'Collatz Bitwise Parity Blocks (n=1 to {max_n})', fontsize=12, fontweight='bold')
plt.yticks(range(max_n), range(1, max_n + 1))
plt.tight_layout()

folderName = str(max_n)
if not os.path.exists(f'Parity Map/{folderName}'):
    os.makedirs(f'Parity Map/{folderName}')

plt.savefig(f"Parity Map/{folderName}/collatz_parity_map.png", dpi=300)
print(f"Parity map saved to Parity Map/{folderName}/")
plt.show() # This forces the window to appear on your screen