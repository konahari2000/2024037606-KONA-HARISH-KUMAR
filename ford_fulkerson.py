def bfs_capacity(graph, source, sink, parent):
    visited = set()
    queue = [source]
    while queue:
        u = queue.pop(0)
        for v, capacity in graph[u].items():
            if v not in visited and capacity > 0:
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
                queue.append(v)
    return False

def ford_fulkerson(graph, source, sink):
    parent = {}
    max_flow = 0

    while bfs_capacity(graph, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow

# Example usage
graph = {
    's': {'a': 10, 'b': 5},
    'a': {'b': 15, 't': 10},
    'b': {'t': 10},
    't': {}
}
print(ford_fulkerson(graph, 's', 't'))
