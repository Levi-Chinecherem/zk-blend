import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create cyclic group of order 3
G = nx.DiGraph()
G.add_nodes_from(range(3))
G.add_edges_from([(i, (i + 1) % 3) for i in range(3)])

# Position nodes in a triangle
pos = {0: (0, 0), 1: (1, 0), 2: (0.5, 1)}

# Set up figure
fig, ax = plt.subplots()
nx.draw(G, pos, with_labels=True, node_color='lightblue', ax=ax)

# Animation function
def update(frame):
    ax.clear()
    nx.draw(G, pos, with_labels=True, node_color='lightblue', ax=ax, edge_color='black')
    current_edge = [(i, (i + 1) % 3) for i in range(3)][frame % 3]
    nx.draw_networkx_edges(G, pos, edgelist=[current_edge], edge_color='red', ax=ax)

# Create animation
ani = FuncAnimation(fig, update, frames=range(3), interval=1000)
plt.title("Cayley Graph: Cyclic Group of Order 3")
plt.show()