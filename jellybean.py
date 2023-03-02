import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_node("A:0")
G.add_node("B:1")
G.add_node("C:0")
G.add_node("D:2")
G.add_node("E:1")
G.add_node("F:3")
G.add_node("G:0")
G.add_node("H:2")
G.add_node("I:4")
G.add_node("J:1")
G.add_node("K:3")
G.add_node("L:0")
G.add_node("M:2")
G.add_node("N:1")
G.add_edge("A:0","B:1")
G.add_edge("B:1","C:0")
G.add_edge("B:1","D:2")
G.add_edge("C:0","E:1")
G.add_edge("D:2","E:1")
G.add_edge("D:2","F:3")
G.add_edge("E:1","G:0")
G.add_edge("E:1","H:2")
G.add_edge("F:3","H:2")
G.add_edge("F:3","I:4")
G.add_edge("G:0","J:1")
G.add_edge("H:2","J:1")
G.add_edge("H:2","K:3")
G.add_edge("I:4","K:3")
G.add_edge("J:1","L:0")
G.add_edge("J:1","M:2")
G.add_edge("K:3","M:2")
G.add_edge("L:0","N:1")
G.add_edge("M:2","N:1")
G.add_edge("N:1","O:0")

print("Nodes:")
print()
print(G.nodes())
print()

print("Edges:")
print()
print(G.edges())
print()

pos = {"A:0": (0, 8), 
       "B:1": (1, 7), 
       "C:0": (0, 6), "D:2": (2, 6),
       "E:1": (1, 5), "F:3": (3, 5),
       "G:0": (0, 4), "H:2": (2, 4), "I:4": (4, 4),
       "J:1": (1, 3), "K:3": (3, 3),
       "L:0": (0, 2), "M:2": (2, 2),
       "N:1": (1, 1),
       "O:0": (0, 0)}

nx.draw_networkx_nodes(G, pos, node_color='#90EE90', node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edge_color='r', arrows = True, arrowsize=20)

paths = nx.all_shortest_paths(G, "A:0", "O:0")
total_paths = 0

print("Paths:")
print()
for path in paths:
    print(path)
    total_paths += 1
    print()

print("Number of Paths: ", total_paths)

plt.show()

