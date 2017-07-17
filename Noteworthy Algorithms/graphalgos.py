from graph import Graph
from collections import deque

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
    airports.add_edge(DFW, JFK, 5)
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

