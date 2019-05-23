from domain.individuo import Individuo
from random import random

class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
    
    
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