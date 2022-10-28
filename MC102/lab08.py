# ENUNCIADO: https://susy.ic.unicamp.br:9999/mc102/08/enunciado.html
###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: Felipe Camilo de Queiroz
# RA: 222006
###################################################

# Leitura da palavra

segredo = ""
palavra = input()
for i in palavra:
    segredo += '_'

# Leitura dos palpites e impressão do resultado para cada palpite

gamewon = False
gamelost = False

tent = 0
while gamewon is False and gamelost is False :
    
    
    palpite = input()
    
    index1 = -1
    index2 = -1
    for letter in palavra:
        index1 += 1
        for i in palpite:
            index2 += 1
            if i == letter and index1 == index2:
                segredo = segredo[:index2]+i.upper()+segredo[index2+1:]
            if i == letter and index1 != index2 and segredo[index2] != palavra[index2].upper():
                segredo = segredo[:index2]+i+segredo[index2+1:]
            if i not in palavra:
                segredo = segredo[:index2]+'_'+segredo[index2+1:]
        index2 = -1        
    index1 = -1 
    
    print(segredo)
        
    tent += 1
    if segredo == palavra.upper():
        gamewon = True
    if tent == 6 and gamewon is False:
        gamelost = True
# Impressão da linha final
if gamewon is True:
    print("Resposta correta")
if gamelost is True:
    print("Palavra correta:", palavra)