from collections import deque

def breadth_first_search(start_vertex, graph):
    open_list = deque([start_vertex])  # FIFO queue
    visited = {start_vertex: True}
    visit_order = []

    while open_list:
        n = open_list.popleft()  # take from front
        visit_order.append(n)

        for m in graph[n]:  # go through neighbors
            if m not in visited:
                open_list.append(m)
                visited[m] = True

    return visit_order

"""
       A
     /   \
    B     C
   / \     \
  D   E     G
       \
        F

"""

"""
Start at 'A'

visit_order = ['A']

Queue (open_list) now has ['B', 'C']

Next: 'B'

visit_order = ['A', 'B']

Add 'D' and 'E' to the queue → ['C', 'D', 'E']

Next: 'C'

visit_order = ['A', 'B', 'C']

Add 'G' → ['D', 'E', 'G']

Next: 'D'

visit_order = ['A', 'B', 'C', 'D']

'D' has no neighbors → nothing added

Next: 'E'

visit_order = ['A', 'B', 'C', 'D', 'E']

Add 'F' → ['G', 'F']

Next: 'G'

visit_order = ['A', 'B', 'C', 'D', 'E', 'G']

'G' has no neighbors → nothing added

Next: 'F'

visit_order = ['A', 'B', 'C', 'D', 'E', 'G', 'F']

'F' has no neighbors → done
"""