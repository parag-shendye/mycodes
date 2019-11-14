import numpy as np
import pylab as pl
import networkx as nx

edges = [(0, 1), (1, 5), (5, 6), (5, 4), (1, 2),
		(1, 3), (9, 10), (2, 4), (0, 6), (6, 7),
		(8, 9), (7, 8), (1, 7), (3, 9)]

goal = 10
G = nx.Graph()
G.add_edges_from(edges)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
pl.show()


# Defining the reward system for actor

MATRIX_SIZE = 11 # from 0 to 10
M = np.matrix(np.ones((MATRIX_SIZE,MATRIX_SIZE)))
M*= -1
#print(M.shape)


