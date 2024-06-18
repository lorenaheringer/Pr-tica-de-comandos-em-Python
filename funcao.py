# Funções: automatizar rotinas que serão utilizadas varias vezes.

# 1. Criação de funções:
# Funcção inicial:
def saudacao():
    print('Seja bem-vindo(a)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')

saudacao()

# Funcao com parametros:
def saudacao(nome, curso):
   print(f'Seja bem-vindo(a)!, {nome}')
   print(f'Olá, é um prazer ter você fazendo parte desse curso de {curso}!')

saudacao('Lorena', 'Python')
saudacao('Rogerio', 'Java')

# Funcao com default:
def saudacao(nome, curso='Python'):
   print(f'Seja bem-vindo(a)!, {nome}')
   print(f'Olá, é um prazer ter você fazendo parte desse curso de {curso}!')

saudacao('Lorena')
saudacao('Lorena', 'C++')

#Funções com retorno:
def soma(num1, num2):
    return num1 + num2

resultado = soma(5,7)

print('O resultado da soma é', resultado)

def calculadora(num1,num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2
    elif operacao == '**':
        return num1 ** num2

resultado = calculadora(2,3,'-')
print('O resultado da operação é: ', resultado)
