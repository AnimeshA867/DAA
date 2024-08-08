import time
import sys
import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        pq = [(0, src)]
        while pq:
            current_distance, u = heapq.heappop(pq)
            for edge in self.graph:
                if edge[0] == u:
                    v = edge[1]
                    weight = edge[2]
                    if dist[v] > current_distance + weight:
                        dist[v] = current_distance + weight
                        heapq.heappush(pq, (dist[v], v))
        return dist

# Input graph
g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

# Measure the time taken to execute the Dijkstra's Algorithm function
start_time = time.time()
distances = g.dijkstra(0)
end_time = time.time()

# Output the result and time taken
print("Vertex distance from Source (0):", distances)
print(f"Time taken to execute the Dijkstra's Algorithm program: {end_time - start_time:.6f} seconds")
print("Program by Animesh")
