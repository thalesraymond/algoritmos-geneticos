from domain.individuo import Individuo
from random import random

class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
        self.lista_solucoes = []
    
    
    def inicializar_populacao(self, espacos, valores, limites_espacos):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(espacos,valores,limites_espacos))
        
        self.melhor_solucao = self.populacao[0]
        
        
    def ordenar_populacao(self):
        self.populacao = sorted(self.populacao, key = lambda populacao: populacao.nota_avaliacao, reverse = True)
        
        
    def obter_melhor_individuo(self, individuo : Individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo
            
    
    def somar_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
            soma += individuo.nota_avaliacao
        
        return soma
    
    
    def selecionar_pai(self, soma_avaliacao):
        pai = -1
        valor_selecionado = random() * soma_avaliacao
        soma = 0;
        i = 0
        
        while i < len(self.populacao) and soma < valor_selecionado:
            soma += self.populacao[i].nota_avaliacao
            pai += 1
            i += 1
        
        return pai;
    
    def visualiza_geracao(self):
        melhor = self.populacao[0]
        print("G: %s -> Valor: %s Espaço: %s Cromossomo: %s" % (self.populacao[0].geracao, 
                                                                melhor.nota_avaliacao,
                                                                melhor.espaco_usado,
                                                                melhor.cromossomo))
        
    def resolver(self, taxa_mutacao, numero_geracoes, espacos, valores, limite_espacos):
        self.inicializar_populacao(espacos, valores, limite_espacos)
        
        for individuo in self.populacao:
            individuo.avaliacao()
            
        self.ordenar_populacao()
        
        self.melhor_solucao = self.populacao[0]
        
        self.lista_solucoes.append(self.melhor_solucao.nota_avaliacao)
        
        self.visualiza_geracao()
        
        for geracao in range(numero_geracoes):
            soma_avaliacao = self.somar_avaliacoes()
            nova_populacao = []
            
            for inividuos_gerados in range(0, self.tamanho_populacao, 2):
                pai1 = self.selecionar_pai(soma_avaliacao)
                pai2 = self.selecionar_pai(soma_avaliacao)
                
                filhos = self.populacao[pai1].crossover(self.populacao[pai2])
                
                nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                nova_populacao.append(filhos[1].mutacao(taxa_mutacao))
                
            self.populacao = list(nova_populacao)
            
            for individuo in self.populacao:
                individuo.avaliacao()
                
            self.ordenar_populacao()
            
            self.visualiza_geracao() 
            
            melhor = self.populacao[0]
            
            self.obter_melhor_individuo(melhor)
            
            self.lista_solucoes.append(melhor.nota_avaliacao)
        
        print("\nMelhor solução -> G: %s Valor: %s Espaço: %s Cromossomo: %s" % (self.melhor_solucao.geracao,
                                                                                 self.melhor_solucao.nota_avaliacao,
                                                                                 self.melhor_solucao.espaco_usado,
                                                                                 self.melhor_solucao.cromossomo))
        
        return self.melhor_solucao.cromossomo
        