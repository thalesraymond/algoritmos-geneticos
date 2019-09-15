from domain.produto import Produto
from domain.algoritmo_genetico import AlgoritmoGenetico
import matplotlib.pyplot as plt

        
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
    
    espacos = []
    valores = []
    nomes = []
    
    for produto in lista_produtos:
        espacos.append(produto.espaco)
        valores.append(produto.valor)
        nomes.append(produto.nome)
        
    limite = 3    
    tamanho_populacao = 20
    fator_mutacao = 0.01
    numero_geracoes = 100
    
    ag = AlgoritmoGenetico(tamanho_populacao)
    
    resultado = ag.resolver(fator_mutacao, numero_geracoes, espacos, valores, limite)
    
    for i in range(len(lista_produtos)):
        if resultado[i] == '1':
            print("Nome: %s R$ %s "  % (lista_produtos[i].nome, lista_produtos[i].valor))
    
#    for valor in ag.lista_solucoes:
#        print(valor)
            
    plt.plot(ag.lista_solucoes)
    plt.title("Acompanhamento dos valores")
    plt.show()
        
        
        
        
        
        