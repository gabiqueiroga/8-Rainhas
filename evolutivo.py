import random
import individuo

class evolutivo:

    def __init__(self, tam_pop, it_max, tx_mut, generation, last_id):
        self.tam_pop = tam_pop
        self.it_max = it_max
        self.tx_mut = tx_mut
        self.generation = generation
        self.last_id = last_id

    def prim_ind(self):
        p_ind = individuo()
        self.last_id = 0
        self.generation = 1
        p_ind.id = 0
        p_ind.generation = 1
        for i in range(8):
            p_ind.board.append(random.randint(0,7))
        return p_ind

    def random_ind(self, last_id, generation):
        r_ind = individuo()
        r_ind.id = self.last_id + 1
        r_ind.generation = self.generation
        for i in range(8):
            r_ind.board.append(random.randint(0,7))
        return r_ind 

    def gera_populacao(self, tam_pop):
        population = []
        for i in range(tam_pop):
            ind = self.random_ind()
            population.append(ind.id)
        return population

    #def fitness(self, ind):
    #    for i in range (8):