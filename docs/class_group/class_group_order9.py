import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Create cyclic group of order 9
G = nx.DiGraph()
G.add_nodes_from(range(9))
G.add_edges_from([(i, (i + 1) % 9) for i in range(9)])

# Position nodes in a circle
pos = {i: (math.cos(2 * math.pi * i / 9), math.sin(2 * math.pi * i / 9)) for i in range(9)}

# Set up figure
fig, ax = plt.subplots()
nx.draw(G, pos, with_labels=True, node_color='lightblue', ax=ax)

# Animation function
def update(frame):
    ax.clear()
    nx.draw(G, pos, with_labels=True, node_color='lightblue', ax=ax, edge_color='black')
    current_edge = [(i, (i + 1) % 9) for i in range(9)][frame % 9]
    nx.draw_networkx_edges(G, pos, edgelist=[current_edge], edge_color='red', ax=ax)

# Create animation
ani = FuncAnimation(fig, update, frames=range(9), interval=1000)
plt.title("Cayley Graph: Cyclic Group of Order 9")
plt.show()