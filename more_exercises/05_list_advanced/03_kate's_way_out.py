from collections import defaultdict


class MazeGraph:

    def __init__(self):
        self.paths = []
        self.path = []
        self.nodes = 0
        self.edges = defaultdict(list)

    def add_edge(self, n, e):
        if max(n, e) > self.nodes:
            self.nodes = max(n, e)

        self.edges[n].append(e)

    def find_path(self, start, end):
        self.paths = []
        self.path = []
        is_visited = [False] * (self.nodes + 1)
        self.find_all_pats(start, end, is_visited)
        return self.paths

    def find_all_pats(self, start, end, is_visited):

        is_visited[start] = True
        self.path.append(start)
        if start == end:
            self.paths.append(self.path.copy())
        else:
            for i in self.edges[start]:
                if is_visited[i] is False:
                    self.find_all_pats(i, end, is_visited)

        self.path.pop()
        is_visited[start] = False


maze = MazeGraph()
lines = int(input())
matrix = []
for _ in range(lines):
    row = [x for x in input()]
    matrix.append(row)

node_id = 1
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 'k':
            matrix[i][j] = 0
        elif matrix[i][j] == ' ':
            matrix[i][j] = node_id
            node_id += 1

end_nodes = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if str(matrix[i][j]).isnumeric():
            # check left
            if j + 1 not in range(len(matrix[0])):
                end_nodes.append(matrix[i][j])
            else:
                if str(matrix[i][j + 1]).isnumeric():
                    maze.add_edge(matrix[i][j], matrix[i][j + 1])
            # check bottom
            if i + 1 not in range(len(matrix)):
                end_nodes.append(matrix[i][j])
            else:
                if str(matrix[i + 1][j]).isnumeric():
                    maze.add_edge(matrix[i][j], matrix[i + 1][j])
            # check right
            if j - 1 not in range(len(matrix[0])):
                end_nodes.append(matrix[i][j])
            else:
                if str(matrix[i][j - 1]).isnumeric():
                    maze.add_edge(matrix[i][j], matrix[i][j - 1])
            # check top
            if i - 1 not in range(len(matrix)):
                end_nodes.append(matrix[i][j])
            else:
                if str(matrix[i - 1][j]).isnumeric():
                    maze.add_edge(matrix[i][j], matrix[i - 1][j])

longest_path = 0
for end_node in end_nodes:
    paths = maze.find_path(0, end_node)
    for path in paths:
        longest_path = max(longest_path, len(path))

if longest_path > 0:
    print(f"Kate got out in {longest_path} moves")
else:
    print("Kate cannot get out")
