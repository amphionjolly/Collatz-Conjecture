# Collatz Conjecture Research Tool

This is a tool designed to help find patterns and do research on the very old and famous mathematical problem of  collatz conjecture.

Rather than relying on calculators or paper, this tool helps generate interactive visual patterns of specific sequence of conjecture, and various other visual functions made using Matplotlab in python. Few visual tools includes 3D landscapes, parity mappings, and complex algebraic network graphs. It has an built in terminal which outputs the computational works, while organizing graphical outputs into auto generated local directories. And also the tool itself runs locally on your device, and it is fully open source.

-----

## The Math behind

The Collatz Conjecture applies the following operation to any positive integer $n$:

```math
f(n) = \begin{cases} 
\frac{n}{2} & \text{if } n \equiv 0 \pmod{2} \\ 
3n + 1 & \text{if } n \equiv 1 \pmod{2} 
\end{cases}
```


To know more about Collatz Conjecture, visit (https://en.wikipedia.org/wiki/Collatz_conjecture)

This tool provides the functions to search for algebraic engines, structural anomalies, and confluence patterns within these determined sequences.

-----

## Main Features

The software includes 8 separate tools to analyse the conjecture of different values and find patterns of it, then visualise them by plotting it in a map, and also to computationaly solve specified conjecture trajectories:

1. **Console Trajectory** (`collatz conjecture.py`): Calculates the step-by-step path of $n$ down to 1, means performs the algorithm of collatz conjecture to the given number and outputs  values of every step.

2. **Quantitative Metrics** (`length & trends.py`): This tool plots the sequence lengths and highest values of conjecture of certain number across a range defined.

3. **Modulo Analysis** (`modulo analyzer.py`): Analyzes the structures or hierarchy of conjecture values based on modulo arithmetics.

4. **Parity Map** (`parity tracker.py`): Generates a 2D map which includes the binary or bitwise parity sections across each step, where the binary value of Even=0 and Odd=1.

5. **Confluence Grid** (`confluence grid[rows link].py`): Generates a grid of map showing the trajectory intersections of values, and plots them as repeating numbers once, directly linking to other conjecture start points.

6. **3D Landscape** (`3d confluence mapping.py`): Generates a 3D topological map of the previous said confluence.

7. **Directed Graph Tree** (`directed graph tree.py`): Visualises the continuing order of value sequences and merging them together when they approach 1,means when ending the conjecture.

8. **Inverse Topology** (`inverse_collatz.py`): This is one is the most useful tool, it operates in reverse of the first tool, meansit  starts at 1 and goes on calculating every valid algeberic predecessing or next values to a specified depth or max/highest value to build a tree structure till that depth.

-----

## Installation & Setup

**Requirements:** Python 3.8+

1. Clone the repository to your local computer.
2. Install the following mathematical and plotting libraries:
   ```bash
   pip install matplotlib numpy networkx
3. Run
   ```bash
   python app.py
