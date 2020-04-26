__all__ = ["criaTabela", "marcaJogada", "atualizaTotal"]

def criaTabela(nome):
    dic =   {
        "nome" : nome,
        "um" : 0,
        "dois" : 0,
        "três" : 0,
        "quatro" : 0,
        "cinco" : 0,
        "seis" : 0,

        "trinca" : 0,
        "quadra" : 0,
        "fullHouse" : 0,
        "seqMin" : 0,
        "seqMax" : 0,
        "yahtzee" : 0,
        "chance" : 0,

        "bônusYahtzee" : 0,

        "total" : 0
        
    }

    #print(dic)

    return dic

def marcaJogada(jogador, escolha, dados):
    dic = {"um": 1, "dois" : 2, "três" : 3, "quatro" : 4, "cinco" : 5, "seis" : 6}
    pontos = dados.count(dic[escolha])*dic[escolha]
    jogador[escolha] = pontos

    #falta pontuar parte inferior
    

def atualizaTotal(jogador):
    limiteBonus = 63
    valorBonus = 35
    pontoSup = ["um", "dois", "três", "quatro", "cinco", "seis"]
    pontoInf = ["trinca", "quadra", "fullHouse", "seqMin",
                "seqMax", "yahtzee", "chance", "bônusYahtzee"]
    totalSup = 0
    totalInf = 0
    for ponto in pontoSup:
        totalSup += jogador[ponto]
    if totalSup >= limiteBonus:
        totalSup += valorBonus
        
    for ponto in pontoInf:
        totalInf += jogador[ponto]

    jogador["total"] = totalSup + totalInf


def analisaPadrao(dados):
    jogadasPossiveis = []
    fullHouseCond2, fullHouseCond3 = False, False
    auxDados = {1 : "um", 2 : "dois", 3 : "tres", 4 : "quatro", 5 : "cinco", 6 : "seis"}

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

    
    
    
    
