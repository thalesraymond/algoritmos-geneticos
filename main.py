from random import random
from domain.produto import Produto
from domain.individuo import Individuo
from domain.algoritmo_genetico import AlgoritmoGenetico

        
if __name__ == '__main__':
    lista_produtos = []
    lista_produtos.append(Produto("Geladeira Dako", 0.751, 999.90))
    lista_produtos.append(Produto("Iphone 6", 0.0000899, 2911.12))
    lista_produtos.append(Produto("TV 55' ", 0.400, 4346.99))
    lista_produtos.append(Produto("TV 50' ", 0.290, 3999.90))
    lista_produtos.append(Produto("TV 42' ", 0.200, 2999.00))
    lista_produtos.append(Produto("Notebook Dell", 0.00350, 2499.90))
    lista_produtos.append(Produto("Ventilador Panasonic", 0.496, 199.90))
    lista_produtos.append(Produto("Microondas Electrolux", 0.0424, 308.66))
    lista_produtos.append(Produto("Microondas LG", 0.0544, 429.90))
    lista_produtos.append(Produto("Microondas Panasonic", 0.0319, 299.29))
    lista_produtos.append(Produto("Geladeira Brastemp", 0.635, 849.00))
    lista_produtos.append(Produto("Geladeira Consul", 0.870, 1199.89))
    lista_produtos.append(Produto("Notebook Lenovo", 0.498, 1999.90))
    lista_produtos.append(Produto("Notebook Asus", 0.527, 3999.00))
    #for produto in lista_produtos:
    #    print(produto.nome)
    
    espacos = []
    valores = []
    nomes = []
    
    for produto in lista_produtos:
        espacos.append(produto.espaco)
        valores.append(produto.valor)
        nomes.append(produto.nome)
        
    limite = 3
    
    tamanho_populacao = 20
    ag = AlgoritmoGenetico(tamanho_populacao)
    ag.inicializar_populacao(espacos,valores,limite)
    
    for individuo in ag.populacao:
        individuo.avaliacao()
    
    ag.ordenar_populacao()
    
    ag.obter_melhor_individuo(ag.populacao[0])
    
    soma = ag.somar_avaliacoes()
    
    print("Melhor solução: %s" % ag.melhor_solucao.cromossomo,
      "Valor: %s\n" % ag.melhor_solucao.nota_avaliacao)
    
    nova_populacao = []
    fator_mutacao = 0.01
    
    for individuos_gerados in range(0, ag.tamanho_populacao, 2):
        pai1 = ag.selecionar_pai(soma)
        pai2 = ag.selecionar_pai(soma)
        
        filhos = ag.populacao[pai1].crossover(ag.populacao[pai2])
        
        nova_populacao.append(filhos[0].mutacao(fator_mutacao))
        nova_populacao.append(filhos[1].mutacao(fator_mutacao))
                
    ag.populacao = list(nova_populacao)
    
    for individuo in ag.populacao:
        individuo.avaliacao()
        
    ag.ordenar_populacao()
    
    ag.obter_melhor_individuo(ag.populacao[0])
    
    soma = ag.somar_avaliacoes()
    
    print("Melhor solução: %s" % ag.melhor_solucao.cromossomo,
          "Valor: %s\n" % ag.melhor_solucao.nota_avaliacao)
    
        
        
        
        
        
        
        