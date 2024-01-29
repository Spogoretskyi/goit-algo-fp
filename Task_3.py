import heapq


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight):
        if weight is None:
            weight = 0
        self.vertices[from_vertex].append((to_vertex, weight))
        self.vertices[to_vertex].append((from_vertex, weight))

    def dijkstra(self, start_vertex):
        distances = {vertex: float("infinity") for vertex in self.vertices}
        distances[start_vertex] = 0

        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


def main():
    metro_graph = Graph()

    metro_graph.add_vertex("Shuliavska")
    metro_graph.add_vertex("Vokzalna")
    metro_graph.add_vertex("Universytet")
    metro_graph.add_vertex("Teatralna")
    metro_graph.add_vertex("Khreshchatyk")
    metro_graph.add_vertex("Arsenalna")
    metro_graph.add_vertex("Hidropark")
    metro_graph.add_vertex("Maidan Nezalezhnosti")
    metro_graph.add_vertex("Poshtova Ploscha")
    metro_graph.add_vertex("Kontraktova Ploscha")
    metro_graph.add_vertex("Plosha Tarasa Shevchenka")
    metro_graph.add_vertex("Lva Tolstogo")
    metro_graph.add_vertex("Olimpiyska")
    metro_graph.add_vertex("Palats Ukraina")
    metro_graph.add_vertex("Lybidska")
    metro_graph.add_vertex("Osokorky")
    metro_graph.add_vertex("Slavutych")
    metro_graph.add_vertex("Vydubichy")
    metro_graph.add_vertex("Druzhby Narodiv")
    metro_graph.add_vertex("Pecherska")
    metro_graph.add_vertex("Klovska")
    metro_graph.add_vertex("Palats Sportu")
    metro_graph.add_vertex("Zoloti Vorota")
    metro_graph.add_vertex("Lukiyanivska")
    metro_graph.add_vertex("Dorogozhychy")

    metro_graph.add_edge("Shuliavska", "Vokzalna", 3),
    metro_graph.add_edge("Vokzalna", "Universytet", 2)
    metro_graph.add_edge("Universytet", "Teatralna", 2)
    metro_graph.add_edge("Teatralna", "Khreshchatyk", 2)
    metro_graph.add_edge("Khreshchatyk", "Arsenalna", 2)
    metro_graph.add_edge("Arsenalna", "Hidropark", 3)
    metro_graph.add_edge("Khreshchatyk", "Maidan Nezalezhnosti", 1)
    metro_graph.add_edge("Maidan Nezalezhnosti", "Poshtova Ploscha", 2)
    metro_graph.add_edge("Poshtova Ploscha", "Kontraktova Ploscha", 2)
    metro_graph.add_edge("Kontraktova Ploscha", "Plosha Tarasa Shevchenka", 2)
    metro_graph.add_edge("Lva Tolstogo", "Maidan Nezalezhnosti", 2)
    metro_graph.add_edge("Olimpiyska", "Lva Tolstogo", 2)
    metro_graph.add_edge("Palats Ukraina", "Olimpiyska", 2)
    metro_graph.add_edge("Lybidska", "Palats Ukraina", 2)
    metro_graph.add_edge("Osokorky", "Slavutych", 3)
    metro_graph.add_edge("Slavutych", "Vydubichy", 4)
    metro_graph.add_edge("Vydubichy", "Druzhby Narodiv", 4)
    metro_graph.add_edge("Druzhby Narodiv", "Pecherska", 3)
    metro_graph.add_edge("Pecherska", "Klovska", 2)
    metro_graph.add_edge("Klovska", "Palats Sportu", 2)
    metro_graph.add_edge("Palats Sportu", "Lva Tolstogo", 1)
    metro_graph.add_edge("Palats Sportu", "Zoloti Vorota", 2)
    metro_graph.add_edge("Zoloti Vorota", "Teatralna", 1)
    metro_graph.add_edge("Zoloti Vorota", "Lukiyanivska", 4)
    metro_graph.add_edge("Lukiyanivska", "Dorogozhychy", 3)

    start_vertex = "Pecherska"
    shortest_distances = metro_graph.dijkstra(start_vertex)

    print(f"Shortest distances from {start_vertex}: {shortest_distances}")


if __name__ == "__main__":
    main()
