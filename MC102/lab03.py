#!/usr/bin/env python
# coding: utf-8

# In[5]:

# ENUNCIADO: https://susy.ic.unicamp.br:9999/mc102/03/enunciado.html
###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Felipe Camilo de Queiroz
# RA: 222006
###################################################

# leitura de dados

diaSemana = int(input())
horaInicio = int(input())
minutoInicio = int(input())
estudante = input()
metodoPagamento = input()

# valor do ingresso inteiro

hora= (horaInicio + minutoInicio/60)

if hora < 18.5:
    if diaSemana == 1:
        ingresso = 30 
        desconto = 0.3
    elif diaSemana == 2:
        ingresso = 15 
        desconto = 0.5
    elif diaSemana == 3:
        ingresso = 15
        desconto = 0.5
    elif diaSemana == 4:
        ingresso = 15
        desconto = 0.5
    elif diaSemana == 5:
        ingresso = 20
        desconto = 0.5
    elif diaSemana == 6:
        ingresso = 20
        desconto = 0.5
    elif diaSemana == 7:
        ingresso = 30
        desconto = 0.2
if hora > 18.5:
    if diaSemana == 1:
        ingresso = 30
        desconto = 0.3
    elif diaSemana == 2:
        ingresso = 20
        desconto = 0.5
    elif diaSemana == 3:
        ingresso = 20
        desconto = 0.5
    elif diaSemana == 4:
        ingresso = 30
        desconto = 0.5
    elif diaSemana == 5:
        ingresso = 30
        desconto = 0.5
    elif diaSemana == 6:
        ingresso = 40
        desconto = 0.3
    elif diaSemana == 7:
        ingresso = 40
        desconto = 0.2
    
# valor a pagar

if estudante == 'S':
    ingresso *= 0.5
elif estudante == 'N':
    if metodoPagamento == 'C':
        ingresso -= ingresso*desconto

# saída do valor do ingresso
print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))

