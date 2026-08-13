# Collatz Conjecture Research Tool

This is a tool designed to help find patterns and eventually solve the very old and famous mathematical problem- the collatz conjecture.

Rather than relying on calculators or paper, this tool helps generate interactive visual patterns of specific sequence of conjecture, and various other visual functions made using Matplotlab in python. Few visual tools includes 3D landscapes, parity mappings, and complex algebraic network graphs. It has an built in terminal which outputs the computational works, while organizing graphical outputs into auto generated local directories. And also the tool itself runs locally on your device, and it is fully open source.

## The Mathematics

The Collatz Conjecture applies the following operation to any positive integer $n$:

$$f(n) = \begin{cases} n/2 & \text{if } n \equiv 0 \pmod{2} \\ 3n + 1 & \text{if } n \equiv 1 \pmod{2} \end{cases}$$

To know more about Collatz Conjecture, visit (https://en.wikipedia.org/wiki/Collatz_conjecture)

This tool provides the functions to search for algebraic engines, structural anomalies, and confluence patterns within these determined sequences.

---

## 🛠️ Execution Matrix (Core Features)

The GUI includes an 8-tool mathematical matrix for analyzing different facets of the sequences:

1. **Console Trajectory** (`collatz conjecture.py`): Calculates the step-by-step path of $n$ down to 1, logging the odd/even transitions.
2. **Quantitative Metrics** (`length & trends.py`): Plots scatter distributions of sequence lengths and peak values (log scale) across a defined range.
3. **Modulo Analysis** (`modulo analyzer.py`): Filters and analyzes the structural classes of numbers based on modulo 3 arithmetic.
4. **Parity Map** (`parity tracker.py`): Generates a 2D binary matrix (Even=0, Odd=1) showing bitwise parity blocks across steps.
5. **Confluence Grid** (`confluence grid[rows link].py`): Maps exact trajectory intersections and plots them as continuous overlapping pathways.
6. **3D Landscape** (`3d confluence mapping.py`): Renders a fully interactive, rotatable 3D topological map charting $n$ against total steps and maximum sequence peaks.
7. **Directed Graph Tree** (`directed graph tree.py`): Visualizes the forward-flowing network of sequences merging as they approach 1.
8. **Inverse Topology** (`inverse_collatz.py`): A heavy computational tool that operates in reverse, starting at 1 and recursively calculating all valid algebraic predecessors to a specified depth to build the infinite tree.

---

## 🚀 Installation & Setup

**Prerequisites:** Python 3.8+

1. Clone the repository to your local machine.
2. Install the required mathematical and plotting libraries:
   ```bash
   pip install matplotlib numpy networkx
3. Run
   ```bash
   python app.py
