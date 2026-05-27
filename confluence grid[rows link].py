import matplotlib.pyplot as plt
import numpy as np
import os
import sys

#ln=int(input("enter the the length of the collatz confluence grid you want to plot="))
if len(sys.argv) > 1:
    ln = int(sys.argv[1])
else:
    ln = 20 # Fallback default

def plot_collatz_paper_grid(max_n):
    # Dictionary to store positions of each number: { number: [(x1, y1), (x2, y2), ...] }
    number_positions = {}
    sequences = {}
    
    # 1. Compute sequences and track exact grid coordinates
    for x in range(1, max_n + 1):
        seq = [x]
        n = x
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            seq.append(n)
        
        sequences[x] = seq
        
        for y_idx, val in enumerate(seq):
            if val not in number_positions:
                number_positions[val] = []
            # Negative y-index forces the paths to go downwards exactly like your paper
            number_positions[val].append((x, -y_idx))
            
    # 2. Initialize plot without using plt.figure()
    fig, ax = plt.subplots(figsize=(12, max(8, max_n)))
    
    # Generate unique colors for each distinct number found in the paths
    unique_numbers = sorted(list(number_positions.keys()))
    color_map = plt.cm.get_cmap('tab20', len(unique_numbers))
    
    # 3. Draw colored tracking loops (lines) connecting identical values
    for idx, val in enumerate(unique_numbers):
        positions = number_positions[val]
        if len(positions) > 1:  # Only connect if the number appears in multiple places
            # Sort from left to right across columns for clean continuous paths
            positions = sorted(positions, key=lambda p: p[0])
            xs = [p[0] for p in positions]
            ys = [p[1] for p in positions]
            
            # Draw the tracking loop line
            ax.plot(xs, ys, color=color_map(idx), alpha=0.7, linewidth=2.5, zorder=1)
            # Add small anchor dots behind the text
            ax.scatter(xs, ys, color=color_map(idx), s=50, zorder=2)

    # 4. Overlay text labels to keep the numbers perfectly readable
    for x, seq in sequences.items():
        # Column Header (Starting Number)
        ax.text(x, 1, f"n = {x}", ha='center', va='center', fontweight='bold', fontsize=12, color='black')
        for y_idx, val in enumerate(seq):
            # Text box with a white background masks the background lines for clean legibility
            ax.text(x, -y_idx, str(val), ha='center', va='center', 
                    bbox=dict(facecolor='white', edgecolor='none', alpha=0.9, pad=2),
                    fontsize=10, fontweight='bold', zorder=3)

    # 5. Grid Formatting
    ax.set_xlim(0.5, max_n + 0.5)
    max_depth = max(len(seq) for seq in sequences.values())
    ax.set_ylim(-max_depth - 0.5, 1.5)
    
    # Remove plot borders and axes to simulate a clean page layout
    ax.axis('off')
    ax.set_title(f"Collatz Confluence Grid (n=1 to {max_n})", fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    folderName=ln
    if not os.path.exists(folderName):
        os.makedirs(f'Confluence Grid/{folderName}',exist_ok=True)
    plt.savefig(f"Confluence Grid/{folderName}/collatz_paper_pattern.svg", bbox_inches='tight') 
    plt.savefig(f"Confluence Grid/{folderName}/collatz_paper_pattern.png", dpi=600)
    #dpi is the quality, higer value is high qual and high storage. keep it 300 as default

# Run the function for your exact requested range
plot_collatz_paper_grid(ln)

plt.show()