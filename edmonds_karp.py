def edmonds_karp(graph, source, sink):
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
            # Check if the reverse edge exists before updating
            if u in graph[v]:
                graph[v][u] += path_flow
            else:
                # If the reverse edge doesn't exist, create it with capacity 0
                graph[v][u] = path_flow
            v = parent[v]
    return max_flow