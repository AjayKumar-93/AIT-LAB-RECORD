import networkx as nx

def a_star_path_finding(graph, startnode, goalnode, heuristic, weight='weight'):
    try:
        path = nx.astar_path(graph, startnode, goalnode, heuristic=heuristic, weight=weight)
        return path
    except nx.NetworkXNoPath:
        return None

if __name__ == "__main__":
    # Define the graph
    G = nx.Graph()
    G.add_edge('S', 'B', weight=3)
    G.add_edge('S', 'A', weight=2)
    G.add_edge('B', 'G', weight=2)
    G.add_edge('A', 'G', weight=1)
    G.add_edge('A', 'S', weight=2)  # Redundant, but fine

    # Heuristic values for each node
    heuristic_values = {
        'S': 5,
        'B': 5,
        'G': 0,
        'A': 2
    }

    # Heuristic function that uses the values
    def example_heuristic(u, v):
        return heuristic_values.get(u, 0)

    # Define start and goal
    start = 'S'
    goal = 'G'

    # Find the path
    path = a_star_path_finding(G, start, goal, example_heuristic)

    if path:
        print(f"Path finding from {start} to {goal}: {path}")
        length = nx.astar_path_length(G, start, goal, heuristic=example_heuristic, weight='weight')
        print(f"Path length: {length}")
    else:
        print(f"No path found from {start} to {goal}")
