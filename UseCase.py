from queue import PriorityQueue

graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'A': 6, 'C': 5, 'D': 2, 'E': 2},
    'C': {'B': 5, 'E': 5},
    'D': {'A': 1, 'B': 2, 'E': 1},
    'E': {'B': 2, 'C': 5, 'D': 1, 'F': 3},
    'F': {'E': 3}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

def a_star_search(start, goal):
    pq = PriorityQueue()
    pq.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    while not pq.empty():
        _, current = pq.get()
        if current == goal:
            break
        for neighbor, cost in graph[current].items():
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                pq.put((priority, neighbor))
                came_from[neighbor] = current
    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from.get(node)
    path.reverse()
    return path, cost_so_far[goal]

start_city = 'A'
goal_city = 'F'
path, cost = a_star_search(start_city, goal_city)
print("Shortest Path:", " → ".join(path))
print("Total Cost:", cost)
