from genetico import Genetico
from individuo import Individuo
from subida import subida

#menuzinho em construção
#não sei se seria legal porque a gente teria que tratar o que está entrando

while True:
    print('O que voce deseja fazer?')
    opcao = int(input('Digite 1 para Algoritmo Genetico ou 2 para subida na encosta e 3 para sair: '))

    match opcao:
        case 1:
            print('Você escolheu Algoritmo Genetico')
            it_max = int(input('Digite o numero maximo de iteracoes: '))
            tam_pop = int(input('Digite o tamanho da populacao: '))
            tx_mut = float(input('Digite o numero da taxa de mutacao: '))
            r = Individuo()
            r = Genetico.random_ind
            print(r)
            opcao1 = int(input('Digite 1 para sair ou qualquer coisa para retornar ao menu principal: '))
            match opcao1:
                case 1:
                    break
                case _:
                    continue
        case 2:
            print('Você escolheu Subida na Encosta')
            it_max = int(input('Digite o número máximo de iterações: '))
            a,b = subida.subida_encosta
            print(a)
            print(b)
            opcao1 = int(input('Digite 1 para sair ou qualquer coisa para retornar ao menu principal: '))
            match opcao1:
                case 1:
                    break
                case _:
                    continue
        case 3:
            break
        case _:
            print('Desculpa, você não digitou algo correspondente às nossas opções.')

