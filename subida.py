from individuo import Individuo

class subida:
    def __init__(self, it_max, atual, melhor_sucessor):
          self.it_max = it_max
          self.atual = atual

    def estado_inicial(self):
        """
        funcao que gera um estado inicial aleatorio
        """
        r_ind = Individuo()
        r_ind.id = self.last_id + 1
        r_ind.generation = self.generation
        for i in range(8):
            r_ind.board.append(random.randint(0,7))
        self.last_id = r_ind.id
        return r_ind

    def aga(self,ind):
        """
        funcao de minimizacao h(x)
        que calcula quantos pares de rainhas estao se atacando
        """
        attack = 0
        k = 0
        j = 1
        for i in range (1,8):
            if ind.board[k] == ind.board[i]:
                attack = attack + 1
            if k == i + j:
                attack = attack + 1
            if k == i - j:
                attack = attack + 1
            j = j + 1
            k = k + 1
        return attack
    
    def melhor_sucessor(self, ind):
        """
        encontra todos os sucessores do estado atual
        e dentre eles calcula qual o que possui o menor número h(x)
        por enquanto incompleta
        """
        melhor = Individuo
        aux = []
        for i in range(8):
            for j in range(8):
                if j == ind.board[i]:
                    continue
        return melhor

    def subida_encosta(self):
        """
        funcao principal
        """
        self.atual = self.estado_inicial()
        it = 1
        vizinho = Individuo()
        while it <= self.it_max:
            vizinho = self.melhor_sucessor(self.atual)
            if self.aga(vizinho) <= self.aga(self.atual):
                self.atual = self.vizinho
        return self.atual
