# Collatz Conjecture Desktop Research Hub

A powerful, native Python GUI application designed for deep mathematical exploration of the Collatz Conjecture (the $3n+1$ problem). 

Rather than relying on static web dashboards, this hub leverages local OS compute power to generate interactive Matplotlib windows, 3D landscapes, parity mappings, and complex algebraic network graphs. It acts as a central command station, piping telemetry directly into a built-in terminal while organizing graphical outputs into dynamically generated local directories.

## The Mathematics

The Collatz Conjecture applies the following operation to any positive integer $n$:

$$f(n) = \begin{cases} n/2 & \text{if } n \equiv 0 \pmod{2} \\ 3n + 1 & \text{if } n \equiv 1 \pmod{2} \end{cases}$$

This laboratory provides the tools to search for algebraic engines, structural anomalies, and confluence patterns within these deterministic sequences.

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
