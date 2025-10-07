import numpy as np

distance_matrix = np.array([
    [0, 2, 2, 5],
    [2, 0, 3, 4],
    [2, 3, 0, 1],
    [5, 4, 1, 0]
])

num_ants = 4
num_iterations = 100  # Set a positive number of iterations
alpha = 1
beta = 2
evaporation_rate = 0.5
pheromone_constant = 1

num_cities = len(distance_matrix)
pheromone = np.ones((num_cities, num_cities))

def calculate_probabilities(current_city, visited, pheromone, distance_matrix):
    probabilities = np.zeros(num_cities)
    for city in range(num_cities):
        if city not in visited:
            probabilities[city] = (pheromone[current_city][city] ** alpha) * ((1 / distance_matrix[current_city][city]) ** beta)
    total = probabilities.sum()
    if total == 0:
        return probabilities
    return probabilities / total

best_path = None
best_distance = float('inf')

for iteration in range(num_iterations):
    all_paths = []
    all_distances = []

    for ant in range(num_ants):
        visited = []
        current_city = np.random.randint(0, num_cities)
        visited.append(current_city)

        while len(visited) < num_cities:
            probabilities = calculate_probabilities(current_city, visited, pheromone, distance_matrix)
            if probabilities.sum() == 0:
                unvisited = [city for city in range(num_cities) if city not in visited]
                next_city = np.random.choice(unvisited)
            else:
                next_city = np.random.choice(range(num_cities), p=probabilities)
            visited.append(next_city)
            current_city = next_city

        visited.append(visited[0])  # Return to start city
        all_paths.append(visited)

        distance = sum(distance_matrix[visited[i]][visited[i + 1]] for i in range(len(visited) - 1))
        all_distances.append(distance)

        if distance < best_distance:
            best_distance = distance
            best_path = visited

    # Evaporate pheromone
    pheromone *= (1 - evaporation_rate)

    # Update pheromone based on all paths
    for path, distance in zip(all_paths, all_distances):
        for i in range(len(path) - 1):
            pheromone[path[i]][path[i + 1]] += pheromone_constant / distance

print("Best Path:", best_path)
print("Best Distance:", best_distance)
