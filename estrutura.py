from tabela import *
from dados import *

__all__ = ["criaJogadores", "controle"]

jogadores = []

numRodadas = 1

def criaJogadores(nomes):
    global jogadores
    for nome in nomes:
        jogadores.append(criaTabela(nome))


def inputRelancar():
    #Essa funcao sera substituida por uma do Interface Grafica
    indexDados = []
    qnt = int(input("Quantos dados relancar? "))
    for i in range(qnt):
        index = int(input("(%d)Qual dado? " % (i+1)))
        indexDados.append(index - 1)
    return indexDados

def inputEscolheJogada():
    #Essa funcao sera substituida por uma do Interface Grafica
    return input("Qual jogada gostaria de fazer? ")
    

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
    escolha = inputEscolheJogada()
    marcaJogada(jogador, escolha, dados)

def vencedor():
    indexVencedor = 0
    n = len(jogadores)
    for i in range(n):
        if jogadores[i]["total"] > jogadores[indexVencedor]["total"]:
            indexVencedor = i
    print("Vencedor: %s" % jogadores[indexVencedor]["nome"])
    
    

def controle():
    global jogadores
    rodada = 0
    while rodada < numRodadas:
        for jogador in jogadores:
            print('Rodada %d - %s' % (rodada+1, jogador["nome"]))
            jogada(jogador)
            print(jogador)
        rodada += 1
    print("////////Fim//////")
    for jogador in jogadores:
        atualizaTotal(jogador)
        print(jogador)
    vencedor()
    
    






        
        



        
        
