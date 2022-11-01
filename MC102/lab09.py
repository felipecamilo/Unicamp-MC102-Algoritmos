# ENUNCIADO: https://susy.ic.unicamp.br:9999/mc102/09/enunciado.html
###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Felipe Camilo de Queiroz
# RA: 222006
###################################################

# Leitura de dados
estoque = {}
controle =  None

while controle!='FIM':
    controle = input()
    
    if controle!= 'FIM':
        separado = controle.split(':')
        N = separado[0][0:-1]
        X = int(separado[1])
        E = estoque.get(N,[0,0,0])
        E[0] += X
        estoque[N]=E
        
        if X< 0 and E[0] >= 0:
            E[2]+=1
        if E[0] < 0:
            print("Quantidade indisponivel para a venda de" , -X , "unidade(s) do produto " + N + ".")
            E[0] -= X
        if X>0:
            E[1]+=1
    
# Impressão da saída
for k,v in sorted(estoque.items()):
    if v[0]>0 or v[1]>0:
        print("Produto: " + k)
        print("Quantidade em Estoque:", v[0])
        print("Pedidos de Compra:", v[1])
        print("Pedidos de Venda:", v[2])