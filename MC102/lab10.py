#ENUNCIADO: https://susy.ic.unicamp.br:9999/mc102/10/enunciado.html

#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome: Felipe Camilo de Queiroz
# RA: 222006
#####################################################

# Leitura da matriz

n = int(input())
matriz = [input().split() for _ in range(n)]

# Leitura e processamento dos caminhos

time1 = input()
M = int(input())
time1points = 0
time2points = 0

for busca in range (M):
    x, y = 0, 0
    rota = input()
    for movimento in rota:
        if movimento == 'N':
            y -= 1
        elif movimento == 'S':
            y += 1
        elif movimento == 'O':
            x -= 1 
        elif movimento == 'L':
            x += 1
            
        if matriz[y][x] == '*' and (busca+1) % 2 == 1:
            time1points += 1
            matriz[y][x] = '.'
            
        if matriz[y][x] == '*' and (busca+1) % 2 == 0:
            time2points += 1
            matriz[y][x] = '.'

# Impressão da saída

if time1 == 'azul':
    print('Tesouros encontrados pelo time azul:', time1points)
    print('Tesouros encontrados pelo time vermelho:', time2points)
    if time1points > time2points:
        print('Vitoria do time azul')
    if time1points < time2points:
        print('Vitoria do time vermelho')
    if time1points == time2points:
        print('Empate')
        
if time1 == 'vermelho':
    print('Tesouros encontrados pelo time azul:', time2points)
    print('Tesouros encontrados pelo time vermelho:', time1points)
    if time2points > time1points:
        print('Vitoria do time azul')
    if time2points < time1points:
        print('Vitoria do time vermelho')
    if time1points == time2points:
        print('Empate')
