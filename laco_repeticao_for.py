# Laços de repetição For (estrutura com nº de repetição definido)
"""
for variavel in range(10):
    print(variavel)
#For vai do valor inicial até 1 unidade menor do valor de parada.    
for variavel in range(1,11):
    print(variavel)
#Range: valor inicial, valor de parada (em 1 unidade a menos), tipo de contagem.
for variavel in range(1,12,2):
    print(variavel)
    
"""
#Exemplo: usando variavel acumuladora
soma = 0

for i in range (1,4):
    nota = float(input(f'Informe a sua nota {i}: '))
    soma = soma + nota

print(soma / 3)
