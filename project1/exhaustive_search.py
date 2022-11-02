from nbformat import write
from Graph import Graph
import itertools
import os, ast, time
from prettytable import PrettyTable


def get_complementary_set(total_vertices, S):
    """ dado uma lista, retorna o complementar dessa lista """
    return list(set(total_vertices) - set(S))


def search(graph):
    """ procurar a(s) solução(soluções) para um dado grafo """
    iterations = 0
    S_all = []              # guardar todas as combinações de S possiveis
    min_cut_edges = {}      # key: S    | value: cut_edges
    len_min_cut = 0         # manter controlo sob o tamanho das edges encontradas

    start = time.time()

    for i in range( 1, len(graph.get_vertices()) + 1 ):
        for subconj in itertools.combinations(graph.get_vertices(), r=i):
            iterations += 1

            S = list(subconj)
            T = get_complementary_set(list(graph.get_vertices().keys()), S)

            # remover o conjunto vazio, o conjunto com todos os vertices e todos aqueles conjuntos onde o seu complementar já está na lista S_all
            if S != [] and S != list(graph.get_vertices().keys()) and T not in S_all: 
                S_all.append(S)

                cut_edges = [ (vert1, vert2)  for vert1 in S   for vert2 in T   if [vert1, vert2] in graph.get_edges() or [vert2, vert1] in graph.get_edges() ]

                if len(min_cut_edges) == 0: 
                    # se o dicionário ainda estiver vazio, adicionar a lista de edges que encontrou
                    min_cut_edges[str(S)] = cut_edges
                    len_min_cut = len(cut_edges)

                elif len(cut_edges) < len_min_cut:
                    # se as edges encontradas tiver um número menor que as edges guardadas no dicionário, atualiza o dicionário com as edges mais pequenas
                    min_cut_edges.clear()
                    min_cut_edges[str(S)] = cut_edges
                    len_min_cut = len(cut_edges)

                elif len(cut_edges) == len_min_cut:
                    # caso sejam do mesmo tamanho, adicionar ao dicionário como uma possível solução
                    min_cut_edges[str(S)] = cut_edges

    exec_time = (time.time() - start)

    return (min_cut_edges, iterations, exec_time)


def write_results(results):
    # se a diretoria escolhida pelo user, não existir, será então criada uma
    
    isExist = os.path.exists('results')
    if not isExist: os.makedirs('results')

    filepath = 'results/exhaustive_search.txt'
    with open(filepath, 'w+') as f:
        t = PrettyTable(['index', 'n', 'prob', 'solutions', 'iterations', 'time (s)'])
        f.write("index n prob solutions iterations time(s)\n")
        for graph, info in results.items():
            n = len(graph.get_vertices())
            prob = graph.get_prob()
            cut_edges = info[0]
            iterations = info[1]
            exec_time = info[2]
            index = list(results.keys()).index(graph) + 1
            t.add_row([index, n, prob, len(cut_edges), iterations, exec_time])
            f.write("%s %s %s %s %s %f\n" % (index, n, prob, len(cut_edges), iterations, exec_time))

        print(t)
    


if __name__ == "__main__":
    prob = [ 0.125, 0.25, 0.50, 0.75 ]
    index = 0
    all_graph = []

    # generate all graphs
    for num_vert in range(2,18):
        for p in prob:
            g = Graph()
            new_graph = g.generate_graph(num_vert, p)
            if new_graph: 
                g.write(index, p)
                all_graph.append(g)
                index += 1
    
    start_time = time.time()

    # find minimum cut
    results = { graph : search(graph) for graph in all_graph }

    total_exec_time = (time.time() - start_time)

    # print all possible minimum cut for all graphs
    for graph, info in results.items(): 
        print("========= Graph", all_graph.index(graph),"=========")

        min_cut = info[0]
        exec_time = info[2]

        for S, cut_edges in min_cut.items():
            print("S =", ast.literal_eval(S))
            print("T =", get_complementary_set(list(graph.get_vertices().keys()), ast.literal_eval(S)))
            print("Minimum cut =", cut_edges)
            print("Execution time =", exec_time)
            print()

    write_results(results)

    print("Execution time =", total_exec_time, "seconds")
