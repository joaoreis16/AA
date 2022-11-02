import matplotlib.pyplot as plt
import os


def plot(x, y, xlabel, ylabel, title, color, type):
    plt.plot(x, y, type, c=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    # plt.show()
    plt.savefig('plots/'+ title +'.png')
    plt.close()


def plot2(info, xlabel, ylabel, title):
    """ info = { label_1: [x1, y1], label_2: [x2, y2] } """
    plt.figure()
    
    # greedy
    label_1 = list(info.keys())[0]
    x1 = info[label_1][0]
    y1 = info[label_1][1]
    plt.plot(x1, y1, 'o', c="blue", label = label_1)
    
    # brute force
    label_2 = list(info.keys())[1]
    x2 = info[label_2][0]
    y2 = info[label_2][1]
    plt.plot(x2, y2, 'x', c="red",label = label_2)
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    plt.legend()
    # plt.show()
    plt.savefig('plots/'+ title +'.png')
    plt.close()

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxx

print("Analysing the results...", end=" ")

# se a diretoria escolhida pelo user, não existir, será então criada uma
isExist = os.path.exists('plots')
if not isExist: os.makedirs('plots')

data_greedy = []
filepath = 'results/greedy_search.txt'
with open(filepath, 'r') as f:
    lines = f.readlines()

    for line in lines:
        info = line[:-1].split(" ")
        data_greedy.append( info )

    data_greedy.pop(0)


data_brute_force = []
filepath = 'results/exhaustive_search.txt'
with open(filepath, 'r') as f:
    lines = f.readlines()

    for line in lines:
        info = line[:-1].split(" ")
        data_brute_force.append( info )

    data_brute_force.pop(0)


values = {}
for info in data_greedy:
    num_vert = int(info[1])
    time = float(info[5])
    if num_vert in values.keys():
        values[num_vert] = (values[num_vert] + time)/2

    else:
        values[num_vert] = time

x = list(values.keys())
y = list(values.values())
plot(x, y, 'Número de vertices (n)', 'Tempo de execução (x10^-6 s)', 'Tempo de execução utilizando Pesquisa Gulosa', 'blue', 'o')


x = [ int(info[1]) for info in data_brute_force ]
y = [ float(info[5]) for info in data_brute_force ]
plot(x, y, 'Número de vertices (n)', 'Tempo de execução (s)', 'Tempo de execução utilizando Pesquisa Exaustiva', 'red', 'o')




x = [ int(info[1]) for info in data_greedy ]
y = [ float(info[4]) for info in data_greedy ]
plot(x, y, 'Número de vertices (n)', 'Iterações', 'Número de iterações utilizando Pesquisa Gulosa', 'blue', '-o')

x = [ int(info[1]) for info in data_brute_force ]
y = [ float(info[4]) for info in data_brute_force ]
plot(x, y, 'Número de vertices (n)', 'Iterações', 'Número de iterações utilizando Pesquisa Exaustiva', 'red', '-o')




x1 = [ int(info[0]) for info in data_greedy ]
y1 = [ float(info[3]) for info in data_greedy ]

x2 = [ int(info[0]) for info in data_brute_force ]
y2 = [ int(info[3]) for info in data_brute_force ]

info = { "greedy": [x1, y1], "brute force": [x2, y2] }
plot2(info, 'Grafos', 'Número de soluções encontradas', 'Número de soluções encontradas em cada grafo')  

print("Done!")