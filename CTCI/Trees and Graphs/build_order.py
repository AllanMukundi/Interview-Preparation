"""
4.7 - You are given a list of projects and a list
of dependencies (which is a list of pairs of projects,
where the second project is dependent on the first project).
All of a project's dependencies must be built before the
project is. Find a build order that will allow the projects
to be built. If there is no valid build order, return an error.
ex: 
    projects: a, b, c, d, e, f
    dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
    output: -> f, e, a, b, d, c
"""

class Graph:

    class _Vertex:

        def __init__(self, x=None):
            self._element = x

        def element(self):
            return self._element

        def __hash__(self):
            return hash(id(self))

    class _Edge:

        def __init__(self, u, v, x=None):
            self._origin = u
            self._destination = v
            self._element = x

        def opposite(self, v):
            return self._origin if v is self._destination else self._origin

    def __init__(self):
        self._outgoing = {}
        self._incoming = {}

    def indeg(self, v):
        return len(self._incoming[v])

    def add_vertex(self, v):
        vertex = self._Vertex(v)
        self._outgoing[vertex.element()] = {}
        self._incoming[vertex.element()] = {}

    def add_edge(self, u, v, x=None):
        e = self._Edge(u, v, x)
        self._incoming[u][v] = e
        self._outgoing[v][u] = e

    def incident_edges(self, v):
        for edge in self._outgoing[v].values():
            yield edge

def build_order(projects, dependencies):
    graph = Graph()
    order = []
    stack = []
    count = {}
    for project in projects:
        graph.add_vertex(project)
    for dependency in dependencies:
        graph.add_edge(dependency[1], dependency[0])
    for vertex in graph._outgoing.keys():
        count[vertex] = graph.indeg(vertex)
        if count[vertex] == 0:
            stack.append(vertex)
    while len(stack) > 0:
        vertex = stack.pop()
        order.append(vertex)
        for edge in graph.incident_edges(vertex):
            opposite = edge.opposite(vertex)
            count[opposite] -= 1
            if (count[opposite] == 0):
                stack.append(opposite)
    if len(order) != len(projects):
        raise ValueError('The given Graph is not a DAG.')
    return order


# Output Tests:
if __name__ == '__main__':
    print(build_order(['a', 'b', 'c', 'd', 'e', 'f'], [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]))

