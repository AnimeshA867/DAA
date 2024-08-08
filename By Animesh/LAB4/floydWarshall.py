import time

def floydWarshall(graph):
    V = len(graph)
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

graph = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]
start_time = time.time()
result = floydWarshall(graph)
end_time = time.time()
print("Shortest distances between every pair of vertices:")
for r in result:
    print(r)
print(f"Time taken: {end_time - start_time:.6f} seconds")
print("Program by Animesh")
