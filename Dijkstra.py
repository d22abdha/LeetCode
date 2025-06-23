import heapq

def dijkstra(graph, start, target):
    # Initialization
    distances = {vertex: float('inf') for vertex in graph}
    previous = {vertex: None for vertex in graph} # Last node on the path
    distances[start] = 0  # Current shortest known distance from A
   
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_vertex]:
            temp_distance = current_distance + weight

            if temp_distance < distances[neighbor]:
                distances[neighbor] = temp_distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (temp_distance, neighbor))

    # Reconstruct path to target
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return distances[target], path


"""
       A
     /   \
   1/     \4
   B       C
    \     /
    2\   /1
       D

"""

"""
 Queue = [(0, A)]

 Step 1: Visit A (distance 0)

Neighbors:

B: 0 + 1 = 1 → Update B

C: 0 + 4 = 4 → Update C

Queue = [(1, B), (4, C)]

Step 2: Visit B (distance 1)

Neighbors:

A: already visited

D: 1 + 2 = 3 → Update D

Queue = [(3, D), (4, C)]

Step 3: Visit D (distance 3)

Neighbors:

B: already visited

C: 3 + 1 = 4 → 4 == 4 → No update

Queue = [(4, C)]

Step 4: Visit C (distance 4)

Neighbors:

A, D → already visited

No updates.

Queue = [] → DONE

"""