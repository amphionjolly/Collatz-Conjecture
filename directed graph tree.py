import networkx as nx
import matplotlib.pyplot as plt


def get_collatz_edges(max_n):
    edges = set()
    for i in range(1, max_n + 1):
        n = i
        while n > 1:
            if n % 2 == 0:
                next_n = n // 2
            else:
                next_n = 3 * n + 1
            edges.add((n, next_n))  # Creates a link from n to its next step
            n = next_n
    return list(edges)

# Settings
max_number = 20  # Keep it low (20-50) at first so the text is readable
edges = get_collatz_edges(max_number)

# Build Graph
G = nx.DiGraph()
G.add_edges_from(edges)

# Plot
plt.figure(figsize=(12, 10))
pos = nx.spring_layout(G, seed=42)  # Generates a clean organic tree layout
nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", 
        font_size=10, font_weight="bold", arrows=True, edge_color="gray")
plt.title(f"Collatz Confluence Tree up to n={max_number}")
plt.show()