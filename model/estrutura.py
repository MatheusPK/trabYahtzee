from tabela import *
from dados import *

__all__ = ["criaJogadores", "controle"]

jogadores = []

numRodadas = 13

def criaJogadores(nomes):
    global jogadores
    for nome in nomes:
        jogadores.append(criaTabela(nome))

def inputNomes():
    #Essa funcao sera substituida por uma do Interface Grafica
    t = []
    n = int(input("Qnts jogadores? "))
    for i in range(n):
        nome = input("Qual nome do jogador %d? " % (i+1))
        t.append(nome)
    return t

def inputRelancar():
    #Essa funcao sera substituida por uma do Interface Grafica
    indexDados = []
    qnt = int(input("Quantos dados relancar? "))
    for i in range(qnt):
        index = int(input("(%d)Qual dado? " % (i+1)))
        indexDados.append(index - 1)
    return indexDados

def inputEscolheJogada(jogadas):
    #Essa funcao sera substituida por uma do Interface Grafica
    print("Qual jogada gostaria de fazer?")
    for i in range(len(jogadas)):
        print("Digite %d para jogada %s" % (i+1, jogadas[i]))
    escolha = int(input())
    return jogadas[escolha-1]

def inputZeraEscolha(jogadas):
    #Essa funcao sera substituida por uma do Interface Grafica
    print("Qual jogada gostaria de zerar?")
    for i in range(len(jogadas)):
        print("Digite %d para jogada %s" % (i+1, jogadas[i]))
    escolha = int(input())
    return jogadas[escolha-1]
    

def jogada(jogador):
    dados = [0, 0, 0, 0, 0]
    numLanc = 3
    n = 1
    lancaDados(dados, [0, 1, 2, 3, 4])
    print(dados)
    while n < numLanc:
        dadosIndex = inputRelancar()
        if dadosIndex == []:
            break
        lancaDados(dados, dadosIndex)
        print(dados)
        n += 1
        
    jogadasPossiveis = analisaPadrao(dados)
    jogadasPossiveis = removeRepetidas(jogador, jogadasPossiveis)
    
    if jogadasPossiveis == []:
        print("Nenhuma jogada disponível!")
        naofeitas = jogadasNaoFeitas(jogador)
        escolha = inputZeraEscolha(naofeitas)
        jogador[escolha] = 0
    else:
        escolha = inputEscolheJogada(jogadasPossiveis)
        marcaJogada(jogador, escolha, dados)
        if escolha == "yahtzee" and jogador[escolha] > 50:
            naofeitas = jogadasNaoFeitas(jogador)
            escolha = inputZeraEscolha(naofeitas)
            jogador[escolha] = 0

def vencedor():
    global jogadores
    indexVencedor = 0
    n = len(jogadores)
    for i in range(n):
        if jogadores[i]["total"] > jogadores[indexVencedor]["total"]:
            indexVencedor = i
    print("Vencedor: %s" % jogadores[indexVencedor]["nome"])
    

def controle():
    global jogadores
    
    nomes = inputNomes()
    criaJogadores(nomes)
    
    rodada = 0
    while rodada < numRodadas:
        for jogador in jogadores:
            print('Rodada %d - %s' % (rodada+1, jogador["nome"]))
            jogada(jogador)
            print(jogador)
        rodada += 1
    print("////////Fim////////")
    for jogador in jogadores:
        atualizaTotal(jogador)
        print(jogador)
    vencedor()
    
    






        
        



        
        
