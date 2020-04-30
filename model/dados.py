import random

__all__ = ["lancaDados", "analisaPadrao"]

def lancaDados(dados, indexDados):
    for i in indexDados:
        dados[i] = random.randint(1, 6)
    
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


    

    
    
    
        
