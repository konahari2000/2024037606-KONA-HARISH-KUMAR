import heapq

def prim(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start)]

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        mst.append((weight, u))

        for v, weight in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (weight, v))
    return mst[1:]  # Exclude the initial dummy edge

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
print(prim(graph, 'A'))
