# ENUNCIADO: https://susy.ic.unicamp.br:9999/mc102/05/enunciado.html

##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome:Felpe Camilo de Queiroz
# RA:222006
##################################################

# Leitura do valor da hora
V = int(input())

# Leitura do numero de dias trabalhados na semana
D = int(input())

# Leitora e processamento dos periodos de trabalho de cada dia

HTTotal = 0
horas_extras = 0
HTDia=0

for i in range(0,D):
    P = int(input())
    for item in range(0,P):
        HI = int(input())
        HF = int(input())
        HTPeriodo = HF - HI
        HTDia += HTPeriodo
        HTTotal += HTPeriodo
        
    if HTDia > 8:
        horas_extras += HTDia-8
    HTDia =0
        
        
Horas_comuns = HTTotal-horas_extras
        
# Calculo do valor devido ao funcionário


if Horas_comuns > 44:
    horas_extras += Horas_comuns-44

valor = (V * HTTotal) + (V/2 * horas_extras) 


# Impressão da saída
print("Horas trabalhadas:", HTTotal)
print("Horas extras:", horas_extras)
print("Valor devido: R$ {:0.2f}".format(valor))
