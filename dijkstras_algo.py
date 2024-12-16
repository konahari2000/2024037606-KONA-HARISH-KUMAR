import heapq

def dijkstra(graph, start):
    min_heap = [(0, start)]
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    while min_heap:
        current_distance, u = heapq.heappop(min_heap)

        if current_distance > distances[u]:
            continue

        for v, weight in graph[u]:
            distance = current_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(min_heap, (distance, v))
    return distances

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
print(dijkstra(graph, 'A'))
