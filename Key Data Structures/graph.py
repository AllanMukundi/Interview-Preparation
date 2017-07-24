"""
An implementation of a Graph using an adjacency map representation.
"""

class Graph:
    """Simple Graph representation using an adjacency map."""

    class Vertex:
        """Lightweight Vertex structure for a Graph."""
        __slots__ = '_element'    # streamline memory usage

        def __init__(self, x):
            """Initializes a Vertex (should not be called directly)."""
            self._element = x

        def element(self):
            """Returns the element associated with the Vertex."""
            return self._element

        def __hash__(self):
            """Allows the Vertex to be used as a dict key."""
            return hash(id(self))

    class Edge:
        """Lightweight Edge structure for a Graph."""
        __slots__ = '_origin', '_destination', '_element'    # streamline memory usage

        def __init__(self, u, v, x):
            """Initializes an Edge (should not be called directly)."""
            self._origin = u
            self._destination = v
            self._element = x

        def element(self):
            """Returns the element associated with the Edge."""
            return self._element

        def opposite(self, v):
            """Returns the Vertex that is opposite v on the Edge."""
            return self._destination if v is self._origin else self._origin

        def endpoints(self):
            """Returns the Edge's endpoints in a tuple (u, v)."""
            return (self._origin, self._destination)

        def __hash__(self):
            """Allows the Edge to be used as a dict key."""
            return hash((self._origin, self._destination))

    def __init__(self, directed=False):
        """Initializes an empty Graph (undirected by default)."""
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        """
        Returns 'True' if the Graph was initialized as 
        a directed Graph and 'False' otherwise.
        """
        return self._incoming is not self._outgoing

    def vertex_count(self):
        """Returns the number of Vertices in the Graph."""
        return len(self._outgoing)

    def vertices(self):
        """Returns an iteration of all of the Vertices in the Graph."""
        return self._outgoing.keys()

    def edge_count(self):
        """Returns the number of Edges in the Graph."""
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else (total // 2)    # avoids double-counting

    def edges(self):
        """Returns a set of all Edges in the Graph."""
        result = set()    # avoids double-counting for undirected Graphs
        for each in self._outgoing.values():
            result.update(each.values())
        return result

    def get_edge(self, u, v):
        """Returns the Edge from u to v, or None if not adjacent."""
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        """
        Returns the number of outgoing Edges incident to Vertex v.
        If the Graph is directed, optional parameter is used to count incoming Edges.
        """
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        """
        Returns all outgoing Edges incident to Vertex v.
        If the Graph is directed, optional parameter is used to request incoming Edges.
        """
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def add_vertex(self, x=None):
        """Inserts and returns a new Vertex with element x."""
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def add_edge(self, u, v, x=None):
        """Inserts and returns a new Edge from u to v with auxiliary element x."""
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
        return e

    def del_vertex(self, v):
        """Removes Vertex v from the Graph."""
        for key in list(self._outgoing[v].keys()):
            self._incoming[key].pop(v, None)
        for key in list(self._incoming[v].keys()):
            self._outgoing[key].pop(v, None)
        self._outgoing.pop(v, None)
        self._incoming.pop(v, None)
        return v

    def del_edge(self, u, v):
        """Removes Edge (u, v) from the Graph (also removes (v, u) if undirected)."""
        edge = self._outgoing[u][v]
        self._outgoing[u].pop(v, None)
        self._incoming[v].pop(u, None)
        return edge

