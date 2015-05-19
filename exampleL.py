#!/usr/bin/env python
"""
An example for Prim's Algorithm
"""
__author__ = """Alberto Barradas (http://github.com/abcsds/)"""

try:
    import matplotlib.pyplot as plt
except:
    raise
try:
    import networkx as nx
except:
    raise

from prim import *

# G=nx.read_edgelist("test.edgelist")
G=nx.read_edgelist("flights.edgelist")

# mst = prim(G,'A')
mst = prim(G,'Madrid')

print "Minimal Spanning Tree: ", mst

pos=nx.spring_layout(G)

# nodes
nx.draw_networkx_nodes(G, pos, node_size=500)

# edges
nx.draw_networkx_edges(G, pos, edgelist=mst, width=6)

# labels
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

plt.axis('off')
plt.savefig("weighted_graph.png") # save as png
plt.show() # display
