class Graph(object):

    def __init__(self, size):
        self.adjMatrix = []
        self.size = size
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])

    def add_edge(self, v1, v2):
        if v1 == v2:
            print(f"Same vertex {v1} and {v2}")
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print(f"No edge between {v1} and {v2}")
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    def print_matrix(self):
        for row in self.adjMatrix:
            print(*row, sep=" ", end="\n")


def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    g.print_matrix()


if __name__ == "__main__":
    main()



