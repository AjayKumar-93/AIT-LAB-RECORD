directed_graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D', 'A'],
    'D': []
}
for node, edges in directed_graph.items():
    for edge in edges:
        print(f"{node} -> {edge}")

        
print("Undirectd graph")
undirected_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C']
}
seen = set()
for node, neighbors in undirected_graph.items():
    for neighbor in neighbors:
        edge = tuple(sorted([node, neighbor]))
        if edge not in seen:
            print(f"{edge[0]} -- {edge[1]}")
            seen.add(edge)
