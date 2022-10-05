###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome: Felipe Camilo de Queiroz
# RA: 222006
###################################################

# leitura da sequência de compras e vendas

x = None
estoque = 0
vendas = 0

while x !=0:
    x = int(input())
    estoque += x
    if x<0 and estoque> 0:
        vendas += 1
    if estoque < 0:
        print('Quantidade indisponível para a venda de %s unidades.' %(-x))
        estoque -= x

# impressão da saída

print('Quantidade de vendas realizadas:',vendas)
print('Quantidade em estoque:',estoque)