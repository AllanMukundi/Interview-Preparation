from graph import Graph
from collections import deque
from heappriorityqueue import HeapPriorityQueue

def dfs(graph, start):
    """
    Performs a DFS on the undiscovered portion 
    of the given Graph from the Vertex start.
    """
    visited, stack = {start: None}, [start]
    while stack:
        vertex = stack.pop()
        for edge in graph.incident_edges(vertex):
            opposite = edge.opposite(vertex)
            if opposite not in visited:
                visited[opposite] = edge
                stack.append(opposite)
    return visited

def bfs(graph, start):
    """
    Performs a BFS on the undiscovered portion
    of the given Graph from the Vertex start.
    """
    visited, queue = {start: None}, deque()
    queue.append(start)
    while queue:
        vertex = queue.popleft()
        for edge in graph.incident_edges(vertex):
            opposite = edge.opposite(vertex)
            if opposite not in visited:
                visited[opposite] = edge
                queue.append(opposite)
    return visited

def path(graph, start, goal):
    """
    Returns a path from the vertex start to the vertex goal via DFS (also works for BFS).
    """
    visited = dfs(graph, start)
    path = []
    if goal in visited:
        path.append(goal)
        walk = goal
        while walk is not start:
            edge = visited[walk]
            parent = edge.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()
    return path

def topological_sort(graph):
    """
    Returns a list of Vertices of the specified Directed Acyclic Graph in topological order.
    Note: if the specified Graph has a cycle, the result will be incomplete.
    """
    topo = []
    ready = []    # Vertices with no remaining constraints
    incount = {}    # tracks indeg(v) for each Vertex
    for each in graph.vertices():
        incount[each] = graph.degree(each, False)    # specifies indeg(v) instead of outdeg(v)
        if (incount[each] == 0):
            ready.append(each)
    while len(ready) > 0:
        vertex = ready.pop()
        topo.append(vertex)
        for edge in graph.incident_edges(vertex):
            opposite = edge.opposite(vertex)
            incount[opposite] -= 1
            if (incount[opposite] == 0):
                ready.append(opposite)
    return topo 

def djikstra(graph, start):
    """
    Computes the shortest-path distances from the Vertex start to all Vertices of the given Graph.

    The given Graph can be undirected or directed, but must be weighted such that edge.element()
    returns a non-negative weight for each edge e.

    Returns a dictionary mapping every reachable Vertex to its distance from start.
    """
    d = {}
    cloud = {}
    pq = HeapPriorityQueue()
    locate = {}
    for vertex in graph.vertices():
        if vertex is start:
            d[vertex] = 0
        else:
            d[vertex] = float('inf')
        locate[vertex] = pq.add(d[vertex], vertex)
    while not pq.is_empty():
        weight, vertex = pq.remove_min()
        cloud[vertex] = weight
        del locate[vertex]
        for edge in graph.incident_edges(vertex):
            opposite = edge.opposite(vertex)
            if opposite not in cloud:
                cur_weight = edge.element()
                if (d[vertex] + cur_weight < d[opposite]):
                    d[opposite] = d[vertex] + cur_weight
                    pq.update(locate[opposite], d[opposite], opposite)
    return cloud


if __name__ == '__main__':
    airports = Graph(True)
    SFO = airports.add_vertex('SFO')
    LAX = airports.add_vertex('LAX')
    DFW = airports.add_vertex('DFW')
    ORD = airports.add_vertex('ORD')
    JFK = airports.add_vertex('JFK')
    BOS = airports.add_vertex('BOS')
    MIA = airports.add_vertex('MIA')
    airports.add_edge(BOS, SFO, 1)
    airports.add_edge(JFK, SFO, 2)
    airports.add_edge(DFW, SFO, 3)
    airports.add_edge(JFK, BOS, 4)
    airports.add_edge(BOS, JFK, 5)
    airports.add_edge(MIA, LAX, 6)
    airports.add_edge(DFW, LAX, 7)
    airports.add_edge(LAX, ORD, 8)
    airports.add_edge(DFW, ORD, 9)
    airports.add_edge(ORD, DFW, 10)
    airports.add_edge(MIA, DFW, 11)
    airports.add_edge(JFK, DFW, 12)
    airports.add_edge(JFK, MIA, 13)
    airports.add_edge(ORD, MIA, 14)
    airports.add_edge(BOS, MIA, 15)
    dag = Graph(True)
    A = dag.add_vertex('A')
    B = dag.add_vertex('B')
    C = dag.add_vertex('C')
    D = dag.add_vertex('D')
    E = dag.add_vertex('E')
    F = dag.add_vertex('F')
    G = dag.add_vertex('G')
    H = dag.add_vertex('H')
    dag.add_edge(A, C)
    dag.add_edge(A, D)
    dag.add_edge(B, D)
    dag.add_edge(B, F)
    dag.add_edge(C, D)
    dag.add_edge(D, F)
    dag.add_edge(C, E)
    dag.add_edge(E, G)
    dag.add_edge(F, G)
    dag.add_edge(G, H)
    dag.add_edge(F, H)
    dag.add_edge(C, H)
    print(djikstra(airports, MIA))

