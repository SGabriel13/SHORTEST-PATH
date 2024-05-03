import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def shortest_path(self, start, end):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        pq = [(0, start)]
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        return distances[end]

# Example usage
graph = Graph()
graph.add_vertex('ENTRANCE', {'REGISTRAR': 3, 'CASHIER': 5})
graph.add_vertex('REGISTRAR', {'ENTRANCE': 3, 'CASHIER': 4, 'GUIDANCE': 2})
graph.add_vertex('CASHIER', {'ENTRANCE': 5, 'REGISTRAR': 4, 'GUIDANCE': 9, 'CANTEEN': 1})
graph.add_vertex('GUIDANCE', {'REGISTRAR': 2, 'CASHIER': 9, 'CANTEEN': 3})
graph.add_vertex('CANTEEN', {'CASHIER': 1, 'GUIDANCE': 3})

start_vertex = 'ENTRANCE'
end_vertex = 'GUIDANCE'
shortest_distance = graph.shortest_path(start_vertex, end_vertex)
print(f"Shortest distance from {start_vertex} to {end_vertex} is {shortest_distance}")