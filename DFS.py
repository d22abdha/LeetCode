def depth_first_search(start_vertex, graph):
    open_list = [start_vertex]  # stack
    visited = {start_vertex: True}
    visit_order = []

    while open_list:
        n = open_list.pop()  # take from the end (LIFO)
        visit_order.append(n)

        for m in reversed(graph[n]):  # reversed to simulate left-to-right consistent order
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

Stack: ['C', 'B'] 

Next: 'B'

visit_order = ['A', 'B']

Stack: ['C', 'E', 'D']

Next: 'D'

visit_order = ['A', 'B', 'D']

'D' has no neighbors

Stack: ['C', 'E']

Next: 'E'

visit_order = ['A', 'B', 'D', 'E']

'F' is added

Stack: ['C', 'F']

Next: 'F'

visit_order = ['A', 'B', 'D', 'E', 'F']

Stack: ['C']

Next: 'C'

visit_order = ['A', 'B', 'D', 'E', 'F', 'C']

'G' is added

Stack: ['G']

Next: 'G'

visit_order = ['A', 'B', 'D', 'E', 'F', 'C', 'G']

'G' has no neighbors

Stack: empty → done
"""
