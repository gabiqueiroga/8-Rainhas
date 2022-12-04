from individuo import Individuo
import random

class subida:
    def __init__(self, it_max):
          self.it_max = it_max
          self.atual = Individuo()

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
        j = 0
        for k in range(0,8):
            for i in range (k+1,8):
                print(ind.board[k],ind.board[i]+(i-k))
                # Verifica se existem pares na mesma linha horizontal
                if ind.board[k] == ind.board[i]:
                    attack = attack + 1
                # Verifica se na mesma diagonal inferior
                if ind.board[k] == ind.board[i]-(i-k):
                    attack = attack + 1
                # Verifica se na mesma diagonal superior
                if ind.board[k] == ind.board[i]+(i-k):
                    attack = attack + 1
                j+=1
        print(j)
        return attack
    
    def melhor_sucessor(self, ind):
        """
        encontra todos os sucessores do estado atual
        e dentre eles calcula qual o que possui o menor número h(x)
        por enquanto incompleta
        """
        melhor = Individuo()
        aux = []
        for i in range(8):
            for j in range(8):
                if j == ind.board[i]:
                    continue
        return melhor

    def imprimir_tabuleiro(self, ind):
        tabuleiro = self.ind.board
        print('---------------------------------------')
        print(tabuleiro)
        print('---------------------------------------')

    def imprimir_aga(self, ind):
        funcao = self.aga(ind)
        print('---------------------------------------')
        print('O número de individuos que nao se atacam eh: ' + self.aga(ind))
        print('---------------------------------------')

    def subida_encosta(self, it_max):
        """
        funcao principal
        """
        self.atual = self.estado_inicial()
        it = 1
        vizinho = Individuo()
        while it <= it_max:
            vizinho = self.melhor_sucessor(self.atual)
            if self.aga(vizinho) <= self.aga(self.atual):
                self.atual = self.vizinho
            it = it + 1
        self.imprimir_tabuleiro(self.atual)
        self.imprimir_aga(self.imprimir_aga)