from random import random

class Individuo():
    def __init__(self, espacos, valores, limite_espacos, geracao=0):
        self.espacos = espacos
        self.valores = valores
        self.limite_espacos = limite_espacos
        self.nota_avaliacao = 0
        self.espaco_usado = 0
        self.geracao = geracao
        self.cromossomo = []
        
        for i in range(len(espacos)):
            if random() < 0.5:
                self.cromossomo.append("0")
            else:
                self.cromossomo.append("1")
                
                
    def avaliacao(self):
        nota = 0
        soma_espacos = 0
        
        for i in range(len(self.cromossomo)):
           if self.cromossomo[i] == '1':
               nota += self.valores[i]
               soma_espacos += self.espacos[i]
               
        if soma_espacos > self.limite_espacos:
            nota = 1
        self.nota_avaliacao = nota
        self.espaco_usado = soma_espacos
        
        
    def crossover(self, outro_individuo):
        corte = round(random()) * len(self.cromossomo)
        
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        
        filhos = [
                    Individuo(self.espacos,self.valores,self.limite_espacos,self.geracao + 1),
                    Individuo(self.espacos,self.valores,self.limite_espacos,self.geracao + 1)
                 ]
        
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        
        return filhos
    
    def mutacao(self, taxa_mutacao):
        print("Antes %s " % self.cromossomo)
        
        for i in range(len(self.cromossomo)):
            if random() >= taxa_mutacao:
                continue;
            self.cromossomo[i] = "0" if self.cromossomo[i] == "1" else "1"
        
        print ("Depois %s " % self.cromossomo)
                
        return self