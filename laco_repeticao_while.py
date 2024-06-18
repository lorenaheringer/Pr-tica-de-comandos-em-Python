# Laços de repetição While

numero_sorteado = 15

numero_escolhido = int(input('Informe um número entre 1 e 20: '))

while numero_escolhido != numero_sorteado:
    print("Você errou o número! Tente novamente...")
    numero_escolhido = int(input('Informe um número entre 1 e 20: '))

print('Parabens! Você acertou o número.')

# Exemplo 2: Estrutura com contador

contador = 0

while contador < 5:
    print(contador)
    
    contador = contador + 1
