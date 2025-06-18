# Import deque for queue functionality
from collections import deque

# Read the first line of input
first_line = input().split()
number_of_islands = int(first_line[0])
number_of_bridges = int(first_line[1])

# Read bridge connections
graph = [[] for x in range(number_of_islands)]
for x in range(number_of_bridges):
    bridge = input().split()
    island1 = int(bridge[0]) - 1 
    island2 = int(bridge[1]) - 1
    graph[island1].append(island2)
    graph[island2].append(island1)

# Read army sizes
army_sizes = []
for x in range(number_of_islands):
    size = int(input())
    army_sizes.append(size)

# Set up visited list and total army
visited = [False] * number_of_islands
visited[0] = True  
total_army = army_sizes[0]

# Repeat conquest until no new islands can be taken
changed = True
while changed:
    changed = False
    for island in range(number_of_islands):
        if visited[island]:
            for neighbor in graph[island]:
                if not visited[neighbor] and army_sizes[neighbor] < total_army:
                    visited[neighbor] = True
                    total_army += army_sizes[neighbor]
                    changed = True  

# Print the final army size
print(total_army)
