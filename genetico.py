import random
from individuo import Individuo

class Genetico:

    def __init__(self, it_max, tam_pop, tx_mut):
        self.tam_pop = tam_pop
        self.it_max = it_max
        self.tx_mut = tx_mut
        self.generation = 1
        self.last_id = -1

    def random_ind(self, last_id, generation):
        """
        funcao que cria um individuo aleatorio
        o id vai ser gerado a partir do id anterior
        e a geracao sera a geracao atual 
        """
        r_ind = Individuo()
        r_ind.id = self.last_id + 1
        r_ind.generation = self.generation
        for i in range(8):
            r_ind.board.append(random.randint(0,7))
        self.last_id = r_ind.id
        return r_ind 

    def gera_populacao(self, tam_pop):
        """
        funcao responsavel por gerar uma populacao de uma dada geracao e ao final incrementa a geracao
        """
        population = []
        ind = Individuo()
        for i in range(tam_pop):
            ind = self.random_ind()
            population.append(ind.id)
        self.generation = self.generation + 1
        return population

    def fitness(self, individuo):
        """
        funcao fitness que conta quantos pares de rainhas nao estao se atacando
        variavel fit começa com 28, que seria o numero ideal, e para cada par que se ataca
        o valor de fit é diminuido em 1
        """
        fit = 28
        k = 0
        j = 1
        for i in range (1,8):
            if individuo.board[k] == individuo.board[i]:
                fit = fit - 1
            if k == i + j:
                fit = fit - 1
            if k == i - j:
                fit = fit - 1
            j = j + 1
            k = k + 1
        return fit

    def crossover(self):
        pass

    def mutacao(self):
        pass

    def add_populacao(self):
        pass
    
    def alg_genetico(self):
        pass