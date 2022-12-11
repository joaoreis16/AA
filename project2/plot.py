import matplotlib.pyplot as plt
import os


def plot(x, y, xlabel, ylabel, title, color, type):
    plt.plot(x, y, type, c=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig('plots/'+ title +'.png')
    plt.close()


def plot2(info, xlabel, ylabel, title):
    """ info = { label_1: [x1, y1], label_2: [x2, y2] } """
    plt.figure()
    
    label_1 = list(info.keys())[0]
    x1 = info[label_1][0]
    y1 = info[label_1][1]
    plt.plot(x1, y1, 'o', c="blue", label = label_1)
    
    label_2 = list(info.keys())[1]
    x2 = info[label_2][0]
    y2 = info[label_2][1]
    plt.plot(x2, y2, 'x', c="red",label = label_2)
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    plt.legend()
    plt.savefig('plots/'+ title +'.png')
    plt.close()






# #############################################################################################################

print("Analysing the results...", end=" ")

# se a diretoria escolhida pelo user, não existir, será então criada uma
isExist = os.path.exists('plots')
if not isExist: os.makedirs('plots')


data = []
filepath = 'results/karger-stein_algorithm.txt'
with open(filepath, 'r') as f:
    lines = f.readlines()

    for line in lines:
        info = line[:-1].split(" ")
        data.append( info )

    data.pop(0)


values = {}
for info in data:
    num_vert = int(info[0])
    time = float(info[4])
    if num_vert in values.keys():
        values[num_vert] = (values[num_vert] + time)/2
    else:
        values[num_vert] = time


x = list(values.keys())
y = list(values.values())
plot(x, y, 'Número de vertices (n)', 'Tempo de execução (s)', 'Tempo de execução em relação ao número de vértices', 'blue', 'o-')


x = [ int(info[0]) for info in data ]
y = [ int(info[3]) for info in data ]
plot(x, y, 'Número de vertices (n)', 'Iterações', 'Número de iterações em relação ao número de vértices', 'blue', '-o')


x = [ int(info[0]) for info in data ]
y = [ int(info[2]) for info in data ]
plot(x, y, 'Número de vertices (n)', 'Soluções', 'Número de soluções em relação ao número de vértices', 'blue', 'o')


x = [ int(info[2]) for info in data ]
y = [ int(info[3]) for info in data ]
plot(x, y, 'Soluções', 'Iterações', 'Número de iterações em relação ao número de soluções', 'blue', 'o')


x = [ int(info[3]) for info in data ]
y = [ float(info[4]) for info in data ]
plot(x, y, 'Iterações', 'Tempo de execução (s)', 'Tempo de execução em relação ao número de iterações', 'blue', 'o')

x = [ int(info[2]) for info in data ]
y = [ float(info[4]) for info in data ]
plot(x, y, 'Soluções', 'Tempo de execução (s)', 'Tempo de execução em relação ao número de soluções', 'blue', 'o')


x = [ int(info[5]) for info in data ]
y = [ int(info[2]) for info in data ]
plot(x, y, 'Grafos', 'Número de Soluções', 'Número de soluções distribuídas pelos grafos testados', 'blue', 'o')


print("Done!")