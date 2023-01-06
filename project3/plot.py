import json 
import numpy as np
import matplotlib.pyplot as plt

f = open("errors/prob_counter.txt", 'r')
lines = f.readlines()

language = ''
for line in lines:
    if line.startswith(">>"): 
        language = line.split(">>")[1][:-1]
    else:
        data = json.loads(line)

        # extract the absolute error and relative error values
        absolute_errors = [ v['absolute_error'] for v in data.values() ]
        relative_errors = [ v['relative_error'] for v in data.values() ]

        print()
        print(f">> {language}")
        print("Min absolute error:", min(absolute_errors))
        print("Average absolute error:", sum(absolute_errors)/ len(absolute_errors))
        print("Max absolute error:", max(absolute_errors))
        print()
        print("Min relative error:", min(relative_errors))
        print("Average relative error:", sum(relative_errors)/ len(relative_errors))
        print("Max relative error:", max(relative_errors))

        #### plot

        # create the first bar chart for absolute error
        fig, ax = plt.subplots()

        x_pos = [i for i, _ in enumerate(data.keys())]
        ax.bar(x_pos, absolute_errors, width=0.8)

        ax.set_xticks(x_pos)
        ax.set_xticklabels(data.keys())
        ax.set_ylabel('Erro absoluto')
        ax.set_xlabel('Letras')
        ax.set_title('Erro absoluto para a contagem de probabilidade decrescente')
        plt.savefig(f'plots/erro_absoluto_prob_counter_{language}.png')

        # create the second bar chart for relative error
        fig, ax = plt.subplots()

        x_pos = [i for i, _ in enumerate(data.keys())]
        ax.bar(x_pos, relative_errors, width=0.8, color="green")

        ax.set_xticks(x_pos)
        ax.set_xticklabels(data.keys())
        ax.set_ylabel('Erro relativo')
        ax.set_xlabel('Letras')
        ax.set_title('Erro relativo para a contagem de probabilidade decrescente')

        # show the plots
        plt.savefig(f'plots/erro_relativo_prob_counter_{language}.png')
        # plt.show()

print()
print()
print("######################################################################################")

f = open("errors/lossy-count.txt", 'r')
lines = f.readlines()

language = ''
for line in lines:
    if line.startswith(">>"): 
        language = line.split(">>")[1][:-1]
    else:
        data = json.loads(line)

        # extract the absolute error and relative error values
        absolute_errors = [ v['absolute_error'] for v in data.values() ]
        relative_errors = [ v['relative_error'] for v in data.values() ]

        print()
        print(f">> {language}")
        print("Min absolute error:", min(absolute_errors))
        print("Average absolute error:", sum(absolute_errors)/ len(absolute_errors))
        print("Max absolute error:", max(absolute_errors))
        print()
        print("Min relative error:", min(relative_errors))
        print("Average relative error:", sum(relative_errors)/ len(relative_errors))
        print("Max relative error:", max(relative_errors))

        #### plot

        # create the first bar chart for absolute error
        fig, ax = plt.subplots()

        x_pos = [i for i, _ in enumerate(data.keys())]
        ax.bar(x_pos, absolute_errors, width=0.8)

        ax.set_xticks(x_pos)
        ax.set_xticklabels(data.keys())
        ax.set_ylabel('Erro absoluto')
        ax.set_xlabel('Letras')
        ax.set_title('Erro absoluto para a contagem de probabilidade decrescente')
        plt.savefig(f'plots/erro_absoluto_lossy_{language}.png')

        # create the second bar chart for relative error
        fig, ax = plt.subplots()

        x_pos = [i for i, _ in enumerate(data.keys())]
        ax.bar(x_pos, relative_errors, width=0.8, color="green")

        ax.set_xticks(x_pos)
        ax.set_xticklabels(data.keys())
        ax.set_ylabel('Erro relativo')
        ax.set_xlabel('Letras')
        ax.set_title('Erro relativo para a contagem de probabilidade decrescente')

        # show the plots
        plt.savefig(f'plots/erro_relativo_lossy_{language}.png')
        # plt.show()