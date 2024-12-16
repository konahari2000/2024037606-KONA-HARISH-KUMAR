def floyd_warshall(graph):
    dist = [[float('inf')] * len(graph) for _ in range(len(graph))]
    for i in range(len(graph)):
        dist[i][i] = 0
    for u in range(len(graph)):
        for v, weight in graph[u]:
            dist[u][v] = weight

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

# Example usage
graph = [
    [(1, 3), (2, 5)],  # From node 0 to node 1 (weight 3), and node 2 (weight 5)
    [(2, 1)],          # From node 1 to node 2 (weight 1)
    []                 # Node 2 has no outgoing edges
]
print(floyd_warshall(graph))
