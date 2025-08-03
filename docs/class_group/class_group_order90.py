import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Create cyclic group of order 90
G = nx.DiGraph()
G.add_nodes_from(range(90))
G.add_edges_from([(i, (i + 1) % 90) for i in range(90)])

# Position nodes in a circle
pos = {i: (math.cos(2 * math.pi * i / 90), math.sin(2 * math.pi * i / 90)) for i in range(90)}

# Set up figure
fig, ax = plt.subplots(figsize=(10, 10))
nx.draw(G, pos, with_labels=True, node_color='lightblue', ax=ax, node_size=100, font_size=8)

# Animation function
def update(frame):
    ax.clear()
    nx.draw(G, pos, with_labels=True, node_color='lightblue', ax=ax, edge_color='black', node_size=100, font_size=8)
    current_edge = [(i, (i + 1) % 90) for i in range(90)][frame % 90]
    nx.draw_networkx_edges(G, pos, edgelist=[current_edge], edge_color='red', ax=ax)

# Create animation
ani = FuncAnimation(fig, update, frames=range(90), interval=200)
plt.title("Cayley Graph: Cyclic Group of Order 90")
plt.show()