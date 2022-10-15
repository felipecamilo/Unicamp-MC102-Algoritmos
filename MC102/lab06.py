# ENUNCIADO: https://susy.ic.unicamp.br:9999/mc102/06/enunciado.html

##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome: Felipe Camilo de Queiroz
# RA: 222006
##################################################

# Leitura da torre de panquecas

torre = [int(panqueca) for panqueca in input().split()]

# Leitura e processamento dos movimentos

M = None
torreFinal = []

while M != 0:
    M = int(input())
    if M!=0:
        torretrocada=torre[M-1::-1]
        for i in range(0, M):
            torre[i]=torretrocada[i]
    

# Impressão da saída

ordemCorreta = sorted(torre)

if torre == ordemCorreta:
    print('Torre estavel')
else:
    print('Torre instavel')
