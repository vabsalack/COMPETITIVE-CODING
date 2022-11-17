from collections import defaultdict


def DFS(graph, start, visited=None):
    """ Depth First Search algo, input->(graph ds, any node)"""

    if visited is None:
        visited = set()

    if start in visited:
        return

    visited.add(start)

    for vertex in graph[start] - set(visited):
        DFS(graph, vertex, visited)

    return visited


def map_graph():
    """ Function to map Graph DS from input's"""
    graph = defaultdict(set)

    nv = int(input("> no of vertices? "))
    ne = int(input("> no of edges? "))

    print("> Input adjacent vertices 'v1 v2': ")
    while ne:
        v1, v2 = list(map(int, input().split()))
        graph[v1].add(v2)
        graph[v2].add(v1)
        ne -= 1

    print('vertices: ', ne, '\n',
          'edges: ', ne, '\n',
          graph)

    return graph


def main():
    graph = map_graph()
    vertices = DFS(graph, list(graph.keys())[0])
    print(*vertices, sep=" ")


if __name__ == "__main__":
    main()
