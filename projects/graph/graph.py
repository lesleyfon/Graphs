"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        pass  # TODO

        if v1 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        pass  # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        q = Queue()
        if starting_vertex in self.vertices:
            q.enqueue(starting_vertex)

        while len(q.queue) > 0:

            dequeue_vert = q.dequeue()
            if dequeue_vert not in visited:

                print(dequeue_vert)

                visited.add(dequeue_vert)

                for neighbors in self.get_neighbors(dequeue_vert):
                    q.enqueue(neighbors)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        pass  # TODO

        visited = set()
        s = Stack()

        if starting_vertex in self.vertices:
            s.push(starting_vertex)

        while s.size() > 0:
            current_pop_vert = s.pop()

            if current_pop_vert not in visited:
                print(current_pop_vert)
                visited.add(current_pop_vert)
                for neighbors in self.vertices[current_pop_vert]:
                    s.push(neighbors)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        s = Stack()

        if starting_vertex in self.vertices:
            s.push(starting_vertex)

        if s.size() == 0:
            return

        current_pop_vert = s.pop()

        if current_pop_vert not in visited:

            visited.add(current_pop_vert)

            for neighbors in self.vertices[current_pop_vert]:
                self.dft_recursive(neighbors)

        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO
        # Create an empty queue and enqueue the PATH TO starting_vertex
        # Create an empty set to track visited verticies
        # while the queue is not empty:
        # get current vertex PATH (dequeue from queue)
        # set the current vertex to the LAST element of the PATH
        # Check if the current vertex has not been visited:

        # CHECK IF THE CURRENT VERTEX IS DESTINATION
        # IF IT IS, STOP AND RETURN
        # Mark the current vertex as visited
        # Add the current vertex to a visited_set
        # Queue up NEW paths with each neighbor:
        # take current path
        # append the neighbor to it
        # queue up NEW path
        pass  # TODO
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
        while q.size() > 0:
            path = q.dequeue()

            v = path[-1]
            if v not in visited:
                visited.add(v)

                if v == destination_vertex:
                    return path
                for neighbors in self.get_neighbors(v):
                    path_copy = list(path)
                    path_copy.append(neighbors)
                    q.enqueue(path_copy)
        return None

        # while q.size() > 0:
        #     current_vert = q.dequeue()
        #     path.append(current_vert)
        #     if current_vert not in visited:

        #         if current_vert == destination_vertex:
        #             return path

        #         visited.add(current_vert)

        #         for neighbors in self.get_neighbors(current_vert):
        #             # path.append(neighbors)
        #             q.enqueue(neighbors)
    def bfs1(self, starting_vertex, destination_vertex):
        queue = Queue()
        queue.enqueue({
            "current_vertex": starting_vertex,
            "path": [starting_vertex]
        })
        visited = set()

        while queue.size() > 0:
            current_obj = queue.dequeue()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']

            if current_vertex not in visited:

                if current_vertex == destination_vertex:
                    print("Current PAth", current_path)
                    return current_path

                visited.add(current_vertex)

                for neighbor in self.vertices[current_vertex]:
                    new_path = list(current_path)
                    new_path.append(neighbor)

                    queue.enqueue({
                        "current_vertex": neighbor,
                        "path": new_path
                    })

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push({
            "current_vertex": starting_vertex,
            'path': [starting_vertex]

        })

        visited = set()

        while stack.size() > 0:
            current_obj = stack.pop()
            current_vertex = current_obj["current_vertex"]
            current_path = current_obj["path"]

            if current_vertex not in visited:

                if destination_vertex == current_vertex:
                    print("Path", current_path)
                    return current_path
                visited.add(current_vertex)

                for neighbors in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(neighbors)
                    stack.push({
                        "current_vertex": neighbors,
                        'path': new_path

                    })

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path)

                if new_path is not None:
                    return new_path
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("bst1", graph.bfs1(6, 4))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

    pass
