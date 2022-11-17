from collections import deque
from DFS_Depth_First_Search import map_graph


def BFS(graph, root):
    visited, queue = list(), deque([root])
    visited.append(root)

    while queue:

        vertex = queue.popleft()

        for adj_nodes in graph[vertex]:
            if adj_nodes not in visited:
                visited.append(adj_nodes)
                queue.append(adj_nodes)

    return visited


def main():
    graph = map_graph()
    bfs_list = BFS(graph, 0)
    print(*bfs_list, sep=" ")


if __name__ == "__main__":
    main()