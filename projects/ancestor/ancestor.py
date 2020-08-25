
vertices = {}


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
    for parent, child in ancestors:
        if child in vertices:
            vertices[child].add(parent)
        else:
            vertices[child] = set()
            vertices[child].add(parent)

    s = Stack()
    visited = set()
    s.push({
        "current_node": starting_node,
        'path': [starting_node]
    })
    possible_paths = []
    while s.size() > 0:
        current_Obj = s.pop()
        current_node = current_Obj["current_node"]
        current_path = current_Obj["path"]

        if current_node not in visited:

            visited.add(current_node)

            if current_node in vertices:

                for parent in vertices[current_node]:
                    new_path = list(current_path)
                    new_path.append(parent)
                    s.push({
                        "current_node": parent,
                        'path': new_path
                    })
            else:

                possible_paths.append(current_path)

    if len(current_path) == 1:
        return -1
    else:
        l = max(map(len, possible_paths))
        return_path = []
        for i in range(len(possible_paths)):
            if len(possible_paths[i]) == l:
                return_path.append(possible_paths[i][-1])
        return min(return_path)


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1), ]
print(earliest_ancestor(ancestors, 6))
print(earliest_ancestor(ancestors, 9))
