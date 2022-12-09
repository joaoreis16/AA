from Graph import Graph
import time, random, math, copy, os, sys

SW_GRAPHS_PATH = "sw_graphs"

""" 
    (1)  the number of basic operations carried out
    (X)  the execution time
    (X)  the number of solutions / configurations tested.
"""

class KargerStein:
    solutions = 0
    iterations = 0

    def get_solutions(self):
        return self.solutions

    def get_iterations(self):
        return self.iterations


    def search(self, graph):
        """ 
        Implementation of Karger-Stein Algorithm 
        """
        g = copy.deepcopy(graph)
        n = len(g.get_vertices())

        if n <= 6: 
            # find a min_cut using normal Karger's Algorithm 
            print(">> Karger's Algorithm (2)")

            # number of solution increases because when the graph has 2 vertices, this is a possible solution
            self.solutions += 1
            return self.find_min_cut(g)      # Karger's Algorithm - until graph reaches 2 vertices

        else:
            # run Karger's Algorithm - until graph reaches t vertices 
            # If we contract from n nodes down to n/sqrt(2) nodes, the probability that we don't contract an edge in the min cut is about 50% !! 
            t = math.floor(1 + (n / math.sqrt(2))) 
            print(">> Karger's Algorithm ("+ str(t) +")")

            g1 = self.contract(g, t)
            g2 = self.contract(g, t)

            return min( self.search(g1), self.search(g2) )


    def contract(self, g, min_vert):
        """
        Implementation of Karger Algorithm but contract the graph until the number of vertices reaches min_vert, and returns the graph contracted
            g - is the original graph
            min_vert - perform the contraction procedure until the graph reaches <min_vert> vertices
        """
        n = len(g.get_vertices())

        while (n > min_vert):
            edges = g.get_edges()
            num_edges = len(g.get_edges())

            if num_edges == 0: break

            r = random.randrange(0, num_edges)
            random_edge = edges[r]

            g.contract_vertices(random_edge)

            n = len(g.get_vertices())

        return g
            

    def find_min_cut(self, graph):
        m = len(graph.get_edges())

        g = self.contract(graph, 2)
        m = min(m, len(g.get_edges())) 
            
        return m


# ############################# MAIN #############################

def main(generate_graphs, inputfile):
    prob = [ 0.125, 0.25, 0.50, 0.75 ]
    index = 0
    all_graph = []

    results_path = 'results/karger-stein_algorithm.txt'
    isExist = os.path.exists(results_path)
    if isExist: os.remove(results_path)

    if generate_graphs:
        for num_vert in range(4,18):
            for p in prob:
                g = Graph()
                new_graph = g.generate_graph(num_vert, p)
                if new_graph: 
                    g.write(index, p)
                    g.set_name("graph" + str(index) +".txt")
                    all_graph.append(g)
                    index += 1

        start_time = time.time()
        results = {}

        for graph in all_graph:
            karger = KargerStein()

            start = time.time()
            min_cut = karger.search(graph)
            end_time = (time.time() - start)

            results[graph] = (min_cut, end_time, karger.get_solutions(), karger.get_iterations())

        total_exec_time = (time.time() - start_time)

        print("\n=============== Results for generated graphs===============")
        for graph, info in results.items(): 
            print(f"{graph.get_name()} | mininum cut: {str(info[0])} | time: {str(info[1])}s | iteractions: {str(info[3])} | solutions: {str(info[2])}")

        print("\nTotal Execution Time = "+ str(total_exec_time) +"s")
        write_results(results)

   
    if inputfile:
        all_graph.clear()
        os.chdir(SW_GRAPHS_PATH)

        if inputfile == "all":
            graph_files = [ fname for fname in os.listdir() ]
        else:
            graph_files = [ fname for fname in os.listdir() if inputfile in fname ]

        open_files = [ open(file, 'r') for file in graph_files ]
        
        for file in open_files:
            graph = {}
            lines = file.readlines()

            if lines[0][:-1] == '0' and lines[1][:-1] == '0':       # se for um grafo que não é orientado nem tem pesos associados
                for line in lines[4:]:
                    line = line[:-1].split(" ")

                    v1, v2 = line[0], line[1]

                    if v1 not in graph.keys():
                        graph[v1] = [v2]

                    elif v1 in graph.keys():
                        graph[v1].append(v2)
                    
                    if v2 not in graph.keys():
                        graph[v2] = [v1]

                    elif v2 in graph.keys():
                        graph[v2].append(v1)

            if graph:
                g = Graph(graph)
                g.set_name(file.name)
                all_graph.append(g)

        os.chdir("..")

        start_time = time.time()
        results = {}

        for graph in all_graph:
            karger = KargerStein()

            start = time.time()
            min_cut = karger.search(graph)
            end_time = (time.time() - start)

            results[graph] = (min_cut, end_time, karger.get_solutions(), karger.get_iterations())

        total_exec_time = (time.time() - start_time)

        print("\n=============== Results for graph instances available on E-Learning ===============")
        for graph, info in results.items(): 
            print(f"{graph.get_name()} | mininum cut: {str(info[0])} | time: {str(info[1])}s | iteractions: {str(info[3])} | solutions: {str(info[2])}")

        print("\nTotal Execution Time = "+ str(total_exec_time) +"s")
        write_results(results)


def write_results(results):
    isExist = os.path.exists('results')
    if not isExist: os.makedirs('results')

    filepath = 'results/karger-stein_algorithm.txt'
    fileExist = os.path.exists(filepath)
    if fileExist: write_type = 'a'
    else: write_type = 'w+'

    with open(filepath, write_type) as f:
        if write_type == 'w+': f.write("n best_solution solutions iterations time(s)\n")
        for graph, info in results.items():
            n = len(graph.get_vertices())   # num vertices
            min_cut = info[0]               # best solution found
            solutions = info[2]             # num solutions tested
            iterations = info[3]            # num iterations
            exec_time = info[1]             # execution time

            f.write("%s %s %s %s %f\n" % (n, min_cut, solutions, iterations, exec_time))

if __name__ == "__main__":
    argv = sys.argv[1:]
    error_msg = """\npython3 karger-stein_algorithm.py -g -f <inputfile: tiny, medium, large, all>\n
        >> Legend (choose one or both)
        -g | if you want to generate and test randomly graphs
        -f | choose the input file you want to test - tiny, medium, large or all\n"""
    inputfile = None
    generate_graphs = False

    for opt in argv:
        if opt == '-h':
            print(error_msg)
            sys.exit()

        elif opt == "-g":
            generate_graphs = True

        elif opt == "-f":
            index = argv.index(opt) + 1
            try:
                inputfile = argv[index]

            except:
                print(error_msg)
                sys.exit()

    if not inputfile and generate_graphs is False: 
        print(error_msg)
        sys.exit()

    main(generate_graphs, inputfile)