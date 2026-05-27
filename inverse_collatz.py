import networkx as nx
import matplotlib.pyplot as plt
import sys
import os

def build_inverse_tree(current_node, current_depth, max_depth, graph):
    if current_depth >= max_depth:
        return

    # Operation 1: The predecessor must be 2n
    even_predecessor = current_node * 2
    graph.add_edge(even_predecessor, current_node)
    build_inverse_tree(even_predecessor, current_depth + 1, max_depth, graph)

    # Operation 2: The predecessor might be (n-1)/3
    # It must be a whole integer, it must be ODD, and it cannot be 1 (to avoid the 1-2-1 loop)
    if (current_node - 1) % 3 == 0:
        odd_predecessor = (current_node - 1) // 3
        if odd_predecessor % 2 != 0 and odd_predecessor > 1:
            graph.add_edge(odd_predecessor, current_node)
            build_inverse_tree(odd_predecessor, current_depth + 1, max_depth, graph)

if len(sys.argv) > 1:
    depth = int(sys.argv[1])
else:
    depth = 12 # Treat the input parameter as 'Depth of Tree' instead of 'Max N' for this tool

G = nx.DiGraph()
print(f"Calculating Inverse Predecessor Tree to Depth: {depth}...")
build_inverse_tree(1, 0, depth, G)

print(f"Generated {len(G.nodes)} predecessor nodes.")

plt.figure(figsize=(14, 10))
# Graphviz 'twopi' layout creates a perfect outward expanding circle from 1
try:
    pos = nx.nx_agraph.graphviz_layout(G, prog="twopi", root=1)
except:
    # Fallback if pygraphviz is not installed
    pos = nx.spring_layout(G, iterations=50, seed=42)

nx.draw(G, pos, with_labels=True, node_size=300, node_color="#ff7f0e", 
        font_size=8, font_weight="bold", arrows=True, edge_color="#333333", alpha=0.9)

plt.title(f"Inverse Collatz Topology (Root: 1, Depth: {depth})", fontsize=14)
plt.tight_layout()

folderName = str(depth)
if not os.path.exists(f'Inverse Tree/{folderName}'):
    os.makedirs(f'Inverse Tree/{folderName}')
plt.savefig(f"Inverse Tree/{folderName}/inverse_tree_depth_{depth}.png", dpi=400)
print("Saved Inverse Tree image.")
plt.show() # Pops the interactive window