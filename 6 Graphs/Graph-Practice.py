        # Graph implementation using Adjacency List

# Space complexity: O (|V| + |E|) 
#                   number of vertices + number of edges
#
# Time Complexity:
    # Adding a new vertex (node): O(1)
    # Adding a new edge (connection): O(1)
    # Removing an edge: O(|E|)
#                       has to iterate through the 
#                       list of edges associated
#                       with the respective vertices
    # Removing a vertex: O(|V| + |E|)
#                       searches through all the vertices 
#                       to also remove the edges 

'''
class Graph:
    def __init__(self):
        self.adj_list = {}


    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])


    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False



my_graph = Graph()
my_graph.add_vertex('G')
my_graph.print_graph()
'''

########################################################
########################################################
########################################################

'''
class Graph:
    def __init__(self):
        self.adj_list = {}


    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
    

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    

my_graph = Graph()
my_graph.add_vertex('G')
my_graph.add_vertex('A')
my_graph.print_graph()
'''

########################################################
########################################################
########################################################

'''
class Graph:
    def __init__(self):
        self.adj_list = {}


    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
    

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    

my_graph = Graph()
my_graph.add_vertex('G')
my_graph.print_graph()
'''

########################################################
########################################################
########################################################

'''
class Graph:
    def __init__(self):
        self.adj_list = {}
    

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
    

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

        
my_graph = Graph()
my_graph.add_vertex('G')
my_graph.print_graph()
'''

########################################################
########################################################
########################################################

'''
class Graph:
    def __init__(self):
        self.adj_list = {}


    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
    

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    

my_graph = Graph()
my_graph.add_vertex('G')
my_graph.add_vertex(0)
my_graph.print_graph()
'''

########################################################
########################################################
########################################################

'''
class Graph:
    def __init__(self):
        self.adj_list = {}


    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
    

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    

my_graph = Graph()
my_graph.add_vertex('G')
my_graph.print_graph()
'''

########################################################
########################################################
########################################################

#'''
class Graph:
    def __init__(self):
        self.adj_list = {}


    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.print_graph()

#'''

########################################################
########################################################
########################################################
