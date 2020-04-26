from estrutura import *

def inputNomes():
    t = []
    n = int(input("Qnts jogadores? "))
    for i in range(n):
        nome = input("Qual nome do jogador %d? " % (i+1))
        t.append(nome)
    return t

nomes = inputNomes()
criaJogadores(nomes)
controle()

#acabar marcaJogada() -> (parteInf, verificar ja feitas, zero)
#arrumar controle/main
#verificar jogadas possiveis


