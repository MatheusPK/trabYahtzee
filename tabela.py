__all__ = ["criaTabela", "marcaJogada",
           "atualizaTotal", "analisaPadrao",
           "removeRepetidas", "jogadasNaoFeitas"]

def criaTabela(nome):
    dic =   {
        "nome" : nome,
        "um" : None,
        "dois" : None,
        "três" : None,
        "quatro" : None,
        "cinco" : None,
        "seis" : None,

        "trinca" : None,
        "quadra" : None,
        "fullHouse" : None,
        "seqMin" : None,
        "seqMax" : None,
        "yahtzee" : None,
        "chance" : None,

        "total" : 0
        
    }

    #print(dic)

    return dic

def marcaJogada(jogador, escolha, dados):
    dic = {"um": 1, "dois" : 2, "três" : 3, "quatro" : 4, "cinco" : 5, "seis" : 6}
    if escolha in dic:
        pontos = dados.count(dic[escolha])*dic[escolha]
    #jogador[escolha] = pontos

    #falta pontuar parte inferior

    if escolha == "trinca" or escolha == "quadra" or escolha == "chance":
        pontos = sum(dados)
    elif escolha == "seqMin":
        pontos = 30
    elif escolha == "seqMax":
        pontos = 40
    elif escolha == "fullHouse":
        pontos = 25
    elif escolha == "yahtzee":
        pontos = 50
        if jogador[escolha] != None:
            pontos = 100
            jogador[escolha] += pontos
            return

    jogador[escolha] = pontos
    

def atualizaTotal(jogador):
    limiteBonus = 63
    valorBonus = 35
    pontoSup = ["um", "dois", "três", "quatro", "cinco", "seis"]
    pontoInf = ["trinca", "quadra", "fullHouse", "seqMin",
                "seqMax", "yahtzee", "chance"]
    totalSup = 0
    totalInf = 0

    for el in jogador:
        if jogador[el] == None:
            jogador[el] = 0
    
    for ponto in pontoSup:
        totalSup += jogador[ponto]
    if totalSup >= limiteBonus:
        totalSup += valorBonus
        print("%s ganhou Bonus Superior!" % jogador["nome"])

    for ponto in pontoInf:
        totalInf += jogador[ponto]

    bonusYahtzee = jogador["yahtzee"] // 100
    print("%s ganhou %d Bonus Yahtzee!" % (jogador["nome"], bonusYahtzee))

    jogador["total"] = totalSup + totalInf


def removeRepetidas(jogador, jogadasPossiveis):
    aux = []
    for el in jogadasPossiveis:
        if jogador[el] == None or el == "yahtzee":
            aux.append(el)
    return aux


def analisaPadrao(dados):
    jogadasPossiveis = ["chance"]
    fullHouseCond2, fullHouseCond3 = False, False
    auxDados = {1 : "um", 2 : "dois", 3 : "três", 4 : "quatro",
                5 : "cinco", 6 : "seis"}

    dados.sort()

    if(dados == [1,2,3,4,5]):
        jogadasPossiveis.append("seqMin")

    if(dados == [2,3,4,5,6]):
        jogadasPossiveis.append("seqMax")

    for i in range(1,7):
        freqDado = dados.count(i) 
        if freqDado > 0:
            jogadasPossiveis.append(auxDados[i])

        if freqDado == 2:
            fullHouseCond2 = True

        elif freqDado == 3:
            jogadasPossiveis.append("trinca")
            fullHouseCond3 = True

        elif freqDado == 4:
            jogadasPossiveis.append("quadra")

        elif freqDado == 5:
            jogadasPossiveis.append("yahtzee")

    if fullHouseCond2 and fullHouseCond3:
            jogadasPossiveis.append("fullHouse")

    return jogadasPossiveis


def jogadasNaoFeitas(jogador):
    escolhas = []
    for el in jogador:
        if jogador[el] == None:
            escolhas.append(el)
    return escolhas

    
    
    
    
