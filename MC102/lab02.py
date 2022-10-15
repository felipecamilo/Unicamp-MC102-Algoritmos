# ENUNCIADO: https://susy.ic.unicamp.br:9999/mc102/02/enunciado.html

D1 = float(input())
V1 = float(input())
T  = float(input())
D2 = float(input())
V2 = float(input())

T1 = D1/V1/24
T2 = (D2/V2/24)+T

if T1<T2:
  print('True')
else:
  print('False')





