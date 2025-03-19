# -*- CP4 - PYTHON -*-
"""
Função em Python

return sempre devolve em tupla

"""
# %%

# Função para calcular média

def calcular_media(lista):
  
    media = sum(lista) / len(lista)
    
    return media

lista = [10, 5, 3, 4, 12]
print(calcular_media(lista))

# %%

# EX 2

def min_max(lista):
    minimo = min(lista)
    maximo = max(lista)
    
    return minimo, maximo

lista = lista = [10, 5, 3, 4, 12]

print(min_max(lista))

x, y = min_max(lista)
print("O valor mínimo:", x)
print("O valor mínimo: ", y)

# %%
# Ex 3
def contar_elementos(lista, elemento):
    contar = lista.count(elemento)
    return contar

numeros = [1, 2, 3, 4 , 5, 1, 2, 3]
alvo = 3

print(contar_elementos(numeros, alvo))


# Ex 4

def inverter_lista(lista):
    inverter = lista[::-1]
    return inverter

numeros = [1, 2, 3, 4 , 5]
print(inverter_lista(numeros))


# Ex 5
def ordenar_lista(lista):
    ordenar = lista == sorted(lista)   # A lista está ordenada?
    return ordenar

numeros = [1, 2, 3, 4, 5]
print(ordenar_lista(numeros))

# %%

# Ex. 6
def remover_numeros_duplicados(lista):
    remover = list(set(lista))

    return remover

numeros = [1, 2, 3, 4 , 5, 1, 2, 3]
sem_valores_duplicados = remover_numeros_duplicados(numeros)
print(sem_valores_duplicados)

# Ex 7 - Retornar numeros postivos e negativos de lista
def positivo_negativo(lista):
    
    positivos = [num for num in lista if num > 0] #Outra forma de escrever uma estrutura de repetição
    negativos = [num for num in lista if num < 0]

    return positivos, negativos

inteiros = [-1, 2, 3, -4 , 5, -7, 2, -3]
print(positivo_negativo(inteiros))

# Para trazer a lista fora da tupla
lista_positivos, lista_negativos = positivo_negativo(inteiros)
print(lista_positivos)
print(lista_negativos)

# %%

# Ex. 8 - Calcular a soma dos quadrados de uma lista
def soma_quadrado(lista):
    eleva_quadrado = sum(num **2 for num in lista)  #Variável num elevado ao quadrado
    return eleva_quadrado

numeros = [6, 1, 3, 2, 4]
print(soma_quadrado(numeros))

# Ex. 9 - Separa palavras curtas

def separar_palavras(lista):
    palavras_curtas = []
    palavras_longas = []
    
    for palavra in lista:
        if len(palavra) < 5: # Quantidade de caracteres até 5
            palavras_curtas.append(palavra)
        else:
            palavras_longas.append(palavra)
    return palavras_curtas, palavras_longas    

lista_palavras = ['sol', 'carro', 'hidrogênio', 'eucalipto', 'lua', 'estrelas', 'carbono']
print(separar_palavras(lista_palavras))
# Separando as informação - tirando do formato de tuplas
curtas, longas = separar_palavras(lista_palavras)
print(curtas)
print(longas)

# %%

# Ex 10 - Função calcular a soma de 3 números ap quadrado
# Um subalgoritmo (função dentro de função)

def quadrado(x):   #Função 1- Eleva ao quadrado
    quadrado = x * x
    return quadrado

def soma_quadrado(x, y, z): #Função 2 - Soma os três valores que foram elevados ao quadrado
     a = quadrado(x) 
     b = quadrado(y)
     c = quadrado(z)
     soma = a + b + c
     return soma

a = -5
b = 2
c = 10

resultado = soma_quadrado(a, b, c)
print(resultado)

# %%

# Ex. 11 - Calcular a área de um retângulo

def area(comprimento, largura):
    a = comprimento * largura
    return a

def mostre_real():
    print("A área do retângulo=", a)
    
altura = float(input("Digite o valor da largura: "))
base = float(input("Digite o valor da altura: "))

ar = area(altura, base)
print(ar)

# %%

# Ex 12 - Calcular soma e média

def soma_valores(lista):
    soma = sum(lista)
    return soma

def calcular_media(lista):
    media = soma_valores(lista) / len(lista)
    return media

lista_valores = [12, 4, 6, 5, 8]
print("A soma dos valroes da lista é ", soma_valores(lista_valores))
print("A média da lista é ", calcular_media(lista_valores))

# %%

# Contar Vogais e Consoantes de cinco palavras de um input feito pelo o usuário


# def contar(palavra):
import pandas as pd

vogais = 'a', 'b'

input_palavra = pd.Series(input("Escreva uma palavra"))



# %%

user_palavra = ['cala']
vogal = "aeiou"

for i in len(user_palavra):
    if user_palavra[i] == vogal:
        i = i+1
print()

#user_palavra = str(input(Digite uma palavra))


# %%

# Definindo lista vazia
palavras = []

# Definindo as vogais (alvo)
vogais = 'aeiou'

# Estrutura de repetição para solicitar 3 palavras para o usuário
for i in range(3):
    user_palavra = str(input("digite 3 palavras: "))
    palavras.append(user_palavra)

# Estrutura de repetição para percorrer cada palavra dentro da lista
for palavra in palavras:
    count_vogais = 0
    count_consoante = 0

# Percorre cada caractere e compara com cada vogal(alvo)
    for letra in palavra:
        # Estrutura de condição
        if letra in vogais:
            # Soma mais 1 para cada vogal dentro da palavra
            count_vogais += 1
        else:
            # Soma mais 1 se não tiver vogal dentro da palavra
            count_consoante += 1

    # Mostra no console as palavras e as suas repectivas quantidades de vogais ou consoantes
    print(f'A palavra {palavra} tem {count_vogais} vogais e {count_consoante} consoantes')

# %%



#Crie um algoritmo selecionar as 3 primeiras letras de palavras que só tiver até 5 letras,
# e as 4 primeiras letras se a palavra tiver mais de 5 letras,
# considerando uma lista com 5 palavras.


# Função para separar entre palavras longas e curtas
def separar_palavras(lista):

    palavras_curtas = []
    palavras_longas = []

# Estrututra de repetição com condição
# Separa as palavras da lista entre curtas (igual ou menor de 5 caracteres) ou longas (maiores que 5)
    for palavra in lista:
        # Se for verdadeira, vai adicionar a palavra na lista de palavras longas
        if len(palavra) <= 5:
            palavras_curtas.append(palavra)
        # Se não, vai adicionar a palavra na lista de palavras curtas
        else:
            palavras_longas.append(palavra)
    return palavras_curtas, palavras_longas

# Função para separar os primeiros caracteres de cada palavra de sua lista
def separar_caracteres(lista1, lista2):
    tresprimeiras = []
    quatroprimeiras = []
    
    #Estrutura de repetição para adicionar as 3 primeiras letras da lista curta para outra lista
    for palavra in lista1:
        tresprimeiras.append(palavra[:3])

    #Estrutura de repetição para adicionar as 4 primeiras letras da lista longa para outra lista
    for palavra in lista2:
        quatroprimeiras.append(palavra[:4])

    return tresprimeiras, quatroprimeiras

# Lista com as palavras
lista_palavras = ['retângulo', 'célula', 'solar', 'lua', 'maçã']

# Defini as variáveis que receberão os valores da primeira função que separa entre longas e curtas 
curtas, longas = separar_palavras(lista_palavras)

# Printa no console os primeiros caracteres de cada um
print("lista de palavras: ", separar_caracteres(curtas, longas))

# %%
# Crie uma função que receba uma lista de palavras e retorne a palavra mais longa.
#Utilize estrutura com input para o usuário.

#definindo lista vazia

def separar_palavras(lista):

    palavras_curtas = []

    palavras_longas = []

#estrutura para definir o que é uma palavra longa e o que é uma curta dividindo em listas separadas

    for palavra in lista:

        if len(palavra) < 6:

            palavras_curtas.append(palavra)

        else:

            palavras_longas.append(palavra)

    return palavras_curtas, palavras_longas
 
#definindo lista vazia

lista_palavras = []
 
#estrutura de repetição para solicitar 5 palavras para o usuario

for i in range(5):

    palavras1 = str(input("escreve as palavras: "))

    lista_palavras.append(palavras1)

#separa as palavras para as listas curtas e longas

curtas, longas = separar_palavras(lista_palavras)
 
#mostra a lista de palavras e a lista de palavras longas no terminal

print("lista com as palavras: ", lista_palavras)

print("a(s) palavra(s) mais longa(a) são: ", longas)
 
