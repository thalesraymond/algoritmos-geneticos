from domain.produto import Produto
from domain.algoritmo_genetico import AlgoritmoGenetico
import matplotlib.pyplot as plt
import pymysql

        
if __name__ == '__main__':
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
    tamanho_populacao = 100
    fator_mutacao = 0.01
    numero_geracoes = 100000
    
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
        
        
        
        
        
        