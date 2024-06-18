# Dicionario

#Criando dicionarios:
dicionario = {}
dicionario = dict()

dicionario = {'nome': 'Walisson', 'idade': 26, 'altura': 1.77}

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos em um dicioanrio

dicionario['programador'] = True
print(dicionario)
dicionario['altura'] = 2
print(dicionario)

# Iteração sobre um dicionario

for chave in dicionario:
    print(chave, dicionario[chave])

# testando a existencia de uma chave
print('peso' in dicionario)
print('altura' in dicionario)