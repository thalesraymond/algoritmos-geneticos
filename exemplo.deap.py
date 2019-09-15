import random
import numpy
from deap import base, creator, algorithms, tools
import matplotlib.pyplot as plt
import pymysql

from domain.produto import Produto
from domain.individuo import Individuo

def avaliacao (individual):
    nota = 0
    soma_espacos = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            nota += valores[i]
            soma_espacos += espacos[i]
    
    if soma_espacos > limite:
        nota = 1
    
    return nota / 100000,

lista_produtos = []
conexao = pymysql.connect(host='localhost', user='root', passwd='root', db='produtos')

cursor = conexao.cursor()
cursor.execute('select nome, espaco, valor, quantidade from produtos')

for produto in cursor:
    for i in range(produto[3]):
        lista_produtos.append(Produto(produto[0], produto[1], produto[2]))

cursor.close()
conexao.close()

espacos = []
valores = []
nomes = []

for produto in lista_produtos:
    espacos.append(produto.espaco)
    valores.append(produto.valor)
    nomes.append(produto.nome)
    
limite = 10    

toolbox = base.Toolbox()
creator.create("FitnessMax", base.Fitness, weights=(1.0, ))
creator.create("Individual", list, fitness= creator.FitnessMax)
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attr_bool, n=len(espacos))

toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", avaliacao) 
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb = 0.01)
toolbox.register("select", tools.selRoulette)

if __name__ == '__main__':
    populacao = toolbox.population(n = 100)
    probabilidade_crossover = 1.0
    probabilidade_mutacao = 0.01
    numero_geracoes = 1000
    estatisticas = tools.Statistics(key=lambda individuo: individuo.fitness.values)
    estatisticas.register("max", numpy.max)
    estatisticas.register("min", numpy.min)
    estatisticas.register("med", numpy.mean)
    estatisticas.register("std", numpy.std)
    
    populacao, info = algorithms.eaSimple(populacao, toolbox, probabilidade_crossover,
                                          probabilidade_mutacao, numero_geracoes,
                                          estatisticas)
    
    melhores = tools.selBest(populacao, 1)
    
    for individuo in melhores:
        print(individuo)
        print(individuo.fitness)
        soma = 0
        for i in range(len(lista_produtos)):
            if individuo[i] == 1:
                soma += valores[i]
                print("nome: %s R$ %s " % (lista_produtos[i].nome, lista_produtos[i].valor))
                
        print("melhor solucao : %s" % soma)
        
    valores_grafico = info.select("max")
    plt.plot(valores_grafico)
    plt.title("Acompanhamento")
    plt.show()
