import networkx as nx
import matplotlib.pyplot as plt
import graph as g

edging = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (2, 5), (2, 4), (2, 6), (3, 6), (2, 7), (1, 7), (7, 6)]
graf = g.create_graph(edging)
g.visualize_graph(graf)