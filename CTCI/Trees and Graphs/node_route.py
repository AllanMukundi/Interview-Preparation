from graph import Graph
from queue import Queue

"""
4.1 - Given a directed graph, design an algorithm to
find out whether there is a route between two nodes.
"""

def is_route(graph, orig, dest):
    visited, queue = set(), Queue()
    visited.add(orig)
    queue.enqueue(orig)
    while (not queue.is_empty()):
        vertex = queue.dequeue()
        for edge in graph.incident_edges(vertex):
            opposite = edge.opposite(vertex)
            if (opposite == dest):
                return True
            elif opposite not in visited:
                visited.add(opposite)
                queue.enqueue(opposite)
    return False


# Unit Tests:
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
    assert(is_route(airports, BOS, MIA) == True)
    assert(is_route(airports, MIA, SFO) == True)
    assert(is_route(airports, SFO, MIA) == False)
    assert(is_route(airports, LAX, JFK) == False)

