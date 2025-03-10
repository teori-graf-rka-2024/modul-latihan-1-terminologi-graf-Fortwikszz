import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    graf = nx.Graph()
    graf.add_edges_from(edges)
    return graf

def get_degree(G: nx.Graph, node: int) -> int:
    return G.degree[node]

def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    visited = set()
    traversal = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            for neighbor in G.neighbors(node):
                dfs(neighbor)

    dfs(start)
    return traversal

def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    visited = set()
    traversal = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            for neighbor in G.neighbors(node):
                if neighbor not in visited:
                    queue.append(neighbor)

def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    try:
        path = nx.shortest_path(G, source=source, target=target, method='dijkstra')
    except nx.NetworkXNoPath:
        path = []
    return path

def visualize_graph(G: nx.Graph) -> None:
    nx.draw(G, with_labels=True)
    plt.show()