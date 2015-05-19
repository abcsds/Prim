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

G=nx.Graph()

G.add_edge('A','B',weight=3)
G.add_edge('A','D',weight=5)
G.add_edge('A','E',weight=9)
G.add_edge('B','C',weight=5)
G.add_edge('B','D',weight=4)
G.add_edge('B','E',weight=8)
G.add_edge('C','D',weight=7)
G.add_edge('C','G',weight=3)
G.add_edge('D','F',weight=8)
G.add_edge('D','G',weight=5)
G.add_edge('D','H',weight=6)
G.add_edge('E','F',weight=2)
G.add_edge('F','H',weight=10)
G.add_edge('G','I',weight=1)
G.add_edge('H','I',weight=3)

mst = prim(G,'A')
othr = [n for n in G.edges() if n not in mst]

print "Minimal Spanning Tree: ", mst

pos=nx.spring_layout(G)

# nodes
nx.draw_networkx_nodes(G, pos, node_size=500)

# edges
nx.draw_networkx_edges(G, pos, edgelist=mst, width=6)
nx.draw_networkx_edges(G, pos, edgelist=othr, width=6, alpha=0.5, edge_color='b', style='dashed')

# labels
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

plt.axis('off')
# plt.savefig("weighted_graph.png") # save as png
plt.show() # display
