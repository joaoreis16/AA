from collections import defaultdict
import random, os
import string
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    graph = {}
    vertices = {}
    edges = []
    alphabet = list(string.ascii_letters)
    prob = 0
    name = ""

    def __init__(self, graph=None):
        if graph is None: graph = {}
        self.graph = graph

    def get_vertices(self):
        return list(self.graph.keys())

    def get_coords(self, vertice):
        return self.vertices[vertice]

    def get_edges(self):
        edges = []
        [ edges.append( [v1, v2] ) for v1 in self.graph for v2 in self.graph[v1] if [v2, v1] not in edges ]
        return edges

    def get_graph(self):
        return self.graph

    def get_edges_by_vertice(self, vertice):
        return self.graph[vertice]

    def are_edges(self, v1, v2):
        if v2 in self.get_edges_by_vertice(v1): return True
        return False

    def get_prob(self):
        return self.prob

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

        
    def generate_graph(self, num_vert, prob):
        self.prob = prob
        self.vertices = self.generate_random_vertices(num_vert)
        self.edges = self.generate_random_edges(num_vert, prob)
        if not len(self.edges): return None

        print("Creating graph with", num_vert, "vertices,", len(self.edges), "edges and prob =", prob)

        for vertice, coords in self.vertices.items():
            for e in self.edges:
                if vertice in e:
                    e.remove(vertice)
                    if vertice in self.graph.keys():
                        self.graph[vertice].append(e[0])
                    else: 
                        self.graph[vertice] = [e[0]]
                    e.append(vertice)

        return self.graph


    def generate_random_vertices(self, num_vert):
        lst_vertices = {}
        for v in range(num_vert):
            while True:
                # evitar que sejam criados vertices que já existem
                coordinates = tuple(random.sample(range(1, 20), 2))
                if coordinates not in lst_vertices:
                    lst_vertices[self.alphabet[v]] = coordinates
                    break

        return lst_vertices


    def generate_random_edges(self, num_vert, prob):
        edges = []

        max_edges = num_vert * (num_vert - 1)/2
        min_edges = num_vert - 1

        num_edges = int(prob * max_edges)
        if num_vert == 2: num_edges = 1     # caso o número de vertices for 2, então o número de arestas irá ser 1

        vert_with_edge = set()      # controlar os vertices que já têm aresta, e evitar que se crie grafos desconexos
        if self.is_a_valid_graph(min_edges, num_edges, max_edges):  # se o grafo for válido, criar as arestas
             for i in range(0, num_edges):
                while True:
                    # evitar que sejam criadas arestas que já existem
                    vertices = random.sample(self.vertices.keys(), 2)
                    reversed_vertices = [ vertices[1], vertices[0] ]

                    if len(vert_with_edge) == len(self.vertices):
                        # caso todos os vertices já tenham pelo menos uma aresta
                        if vertices not in edges and reversed_vertices not in edges:
                            edges.append(vertices)
                            break

                    else:
                        # caso um vertice já tenha sido utilizado, o while true continua até todos os vertices serem utilizados
                        if vertices[0] not in vert_with_edge or vertices[1] not in vert_with_edge:
                            vert_with_edge.update( vertices[0] )
                            vert_with_edge.update( vertices[1] )

                            if vertices not in edges and reversed_vertices not in edges:
                                edges.append(vertices)
                                break


        return edges


    def is_a_valid_graph(self, min, num, max):
        """ 
        Um graph só é grafo válido se o seu número de arestas está entre o mínimo e o máximo de arestas possível:
                                        min_edges <= num_edges <= max_edges 
        """
        return min <= num and num <= max 


    def get_adjacency_matrix(self):
        adjacency_matrix = []
        adjacency_list = defaultdict(list)
        dict_vert = { list(self.vertices.keys())[i]: i  for i in range(len(self.vertices)) }

        for edge in self.edges:
            a, b = edge[0], edge[1]
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        for v, list_v in adjacency_list.items():
            pos = [ dict_vert[adj_v] for adj_v in list_v ]
            row = []
            for i in range(len(self.vertices)):
                if i in pos:
                    row.append(1)
                else:
                    row.append(0)

            adjacency_matrix.append(row)

        return adjacency_matrix


    def write(self, num_graph, prob):
        # se a diretoria escolhida pelo user, não existir, será então criada uma
        isExist = os.path.exists('graphs')
        if not isExist: os.makedirs('graphs')

        filepath = 'graphs/graph'+ str(num_graph) +'.txt'
        with open(filepath, 'w+') as f:
            f.write('vertices = '+ str(self.vertices))
            f.write('\ngraph = '+ str(self.graph))
            f.write('\nprob = '+ str(prob))
            f.write('\nAdjancecy matrix =' + str(self.get_adjacency_matrix()))

        self.plot(num_graph)


    def plot(self, index):
        g = nx.Graph()

        edges = [ (e[0], e[1]) for e in self.get_edges() ]
        g.add_edges_from(edges)

        nx.draw_spring(g, with_labels = True)
        # plt.show()
        plt.savefig('graphs/graph'+ str(index) +'.png')
        plt.close()



## #################### Funções adicionadas no projeto 2 ####################


    def contract_vertices(self, edge):
        v1, v2 = edge[0], edge[1]

        head = self.graph[v1]
        tail = self.graph[v2]

        # remover a aresta (v1,v2)
        head.remove(v2)
        tail.remove(v1)

        head.extend(tail)   # juntar as arestas que estavam ligadas aos nós juntos
        merged_edges = head

        # atualizar o grafo ==> v1 e v2 já não existem, porém v1+v2 é um novo vertice
        self.graph.pop(v1)
        self.graph.pop(v2)

        new_vertice = v1 + v2
        self.graph[new_vertice] = merged_edges

        # atualizar todos os vertices vizinhos da fusão destes 2 vertices
        for vertice, edges in self.graph.items():

            while v1 in edges:   # alterar enquato houver vertices iguais 
                edges.remove(v1)
                if vertice != new_vertice: edges.append(new_vertice) 
                
            while v2 in edges:   # alterar enquato houver vertices iguais 
                edges.remove(v2)
                if vertice != new_vertice: edges.append(new_vertice) 

        return self.graph