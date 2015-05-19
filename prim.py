# Prim Algorithm using networkx
try:
    import networkx as nx
except:
    raise

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

def prim(G,start):
    """Function recives a graph and a starting node, and returns a MST"""
    stopN = G.number_of_nodes() - 1
    openSet = start
    closedSet = set()
    priorityQueue = Q.PriorityQueue() # priorityQueue.put(10) priorityQueue.get()
    mst = []

    while len(mst) < stopN:
        closedSet.add(openSet)




    pass
