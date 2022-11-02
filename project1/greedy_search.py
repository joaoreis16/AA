from Graph import Graph
import ast, time, os
from prettytable import PrettyTable


def get_complementary_set(total_vertices, S):
    """ dado uma lista, retorna o complementar dessa lista """
    return list(set(total_vertices) - set(S))


def search(graph):
    # a heuristica utilizada é a quantidade de arestas que um vertice tem
    iterations = 0
    min_cut_edges = {}      # key: S    | value: cut_edges
    start = time.time()

    heuristics = { v: len(e) for v,e in graph.get_graph().items()}
    sorted_heuristic = dict(sorted(heuristics.items(), key=lambda x: (x[1], x[0])))
    
    # o vertice com menor número de arestas será a solução
    vertice = list(sorted_heuristic.keys())[0]
    S = [vertice]
    cut_edges = [ (vertice, egde)  for egde in graph.get_edges_by_vertice(vertice)  ]
    min_cut_edges[str(S)] = cut_edges

    iterations += 1
    exec_time = (time.time() - start)

    return (min_cut_edges, iterations, exec_time)



def write_results(results):
    # se a diretoria escolhida pelo user, não existir, será então criada uma
    isExist = os.path.exists('results')
    if not isExist: os.makedirs('results')

    filepath = 'results/greedy_search.txt'
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

    results = { graph : search(graph) for graph in all_graph }

    total_exec_time = (time.time() - start_time)

    # print the solutions found
    for graph, info in results.items(): 
        print("========= Graph", all_graph.index(graph),"=========")
        min_cut = info[0]

        for S, cut_edges in min_cut.items():
            print("S =", ast.literal_eval(S))
            print("T =", get_complementary_set(list(graph.get_vertices().keys()), ast.literal_eval(S)))
            print("Minimum cut =", cut_edges)
            print()

    write_results(results)
    print("Execution time =", total_exec_time, "seconds")