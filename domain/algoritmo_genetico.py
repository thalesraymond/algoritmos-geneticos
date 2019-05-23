from domain.individuo import Individuo

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