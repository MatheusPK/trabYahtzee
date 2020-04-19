from estrutura import *

def inputNomes():
    t = []
    n = int(input("Qnts jogadoers? "))
    for i in range(n):
        nome = input("Qual nome do jogador %d? " % (i+1))
        t.append(nome)
    return t

nomes = inputNomes()
criaJogadores(nomes)
controle()


