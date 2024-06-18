# Listas
"""
# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista
notas = [7.9,9.7,8.2]

# Criando listas
lista = []
lista = list()
lista = [18, 'Lorena Heringer', 13550680619, True] # a estrutura de lista em python aceita diferentes tipos de dados em uma única lista.
lista_de_listas = [10, [1,2,3]]

# Indexação e slices (fatiamento)

lista = [10, 'Lorena Heringer', 12345, True]
# Indexação:
print(lista[0]) #imp = indices de listas iniciam em 0.
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[-1]) #imp: -1 imprime o último elemento da lista, -2 o penúltimo, e assim sucessivamente.

# Slices

lista = [10,20,30,40,50,60,70]

print(lista[0:3])
print(lista[3:6])
print(lista[2:])
print(lista[2:6:2])

#Iterações com For:
# 1. Utilizando os próprios elementos da lista.

for elemento in lista:
    print(elemento)

# 2. utilizando os indices:

print('Comprimento da lista:', len(lista)) 

for i in range(len(lista)):
    print(i)

for i in range(len(lista)):
    print(lista[i])
"""
#Métodos de listas: uma função que está atrelada a uma variavel.
lista = [1,3,12,8,2]

#append: adiciona um elemento ao final da lista.
print('Antes do append: ', lista)
lista.append(3)
print('Depois do append: ', lista)
#insert: permite escolher a posição do elemento e seu valor.
lista.insert(2,10)
print('Depois do insert: ', lista)
#extend: une duas listas, jogando a segunda lista no final da primeira.
lista2 = [1,2,3]
lista.extend(lista2)
print('Depois do extend: ', lista)
#pop: remover o elemento especificado pelo indice ou o ultimo indice.
lista.pop()
print('Lista apos o pop: ', lista)
lista.pop(0)
print('Lista spós o pop(0): ', lista)
#remove: passa o valor a ser retirado (elemento). Ele remove o primeiro que encontra.
lista.remove(3)
print('Lista depois do remove:', lista)
#count: quantas quantas vezes o elemento passado como parametro repete-se.
print('Quantidade do valor 2 na lista: ', lista.count(2))
#index: descobre o indice do elemento passado como parametro.
print('Indice do elemento 12: ', lista.index(12))
#sort: ordena a lista de forma crescente ou descrescente.
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

#Funções para listas:

# len: imprime quantos elementos tem na lista.
print(len(lista))
#sum: soma todos os elementos da lista.
print(sum(lista))
#max: imprime o maior elemento.
print('Maior elemento da lista: ', max(lista))
#min: imprime o menor elemento.
print('Menor elemento da lista: ', min(lista))






