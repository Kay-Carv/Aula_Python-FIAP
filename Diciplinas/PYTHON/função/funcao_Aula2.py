# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 08:54:12 2025
FIAP
@author: Kayque Carvalho
Professor: Francisco

## Funções em python - Aula 2
"""

# Ex 1:
    
def quadrado(x):
    y = x * x
    return y

print(quadrado(2))
print(quadrado(3))
print(quadrado(4))

# Função dentro de função
def somaQuadrado(x, y, z, w):
    a = quadrado(x)
    b = quadrado(y)
    c = quadrado(z)
    d = quadrado(w)
    resultado =  a + b + c + d
    return resultado

print(somaQuadrado(2, 3, 4, 5))

# %%

# Ex 2

# Calcular média
def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media

# Classificar desempenho do aluno

def classificar_aluno(notas):
    media = calcular_media(notas)
    
    if media >= 7:
        return 'Aprovado'
    elif 5 <= media < 7:
        return 'Exame'
    else:
        return 'Reprovado'
    
notas_alunos = [8, 7.5, 6]
print(calcular_media(notas_alunos))
print(classificar_aluno(notas_alunos))

# %%

# Exercício 1

"""Crie uma função para solicitar ao usuário 5 notas em função.
A função seguinte deverá utilizar a primeira função para cacular a média
e retornar se o aluno está ou não aprovado."""


def solicitarValores():
    user_notas = []
    for i in range(5):
        valor = float(input("Digite uma nota: "))
        user_notas.append(valor)
    return user_notas
    

def calcular_media(listaNotas):
    media = sum(listaNotas) / len(listaNotas)
    return media

def classificar_aluno(listaNotas):
    media = calcular_media(listaNotas)
    
    if media >= 7:
        return 'Aluno aprovado'
    elif media >= 5:
        return 'Aluno de exame'
    else:
        return 'Aluno reprovado'

# Teste para primeira função

lista = solicitarValores()
print(lista)

# Teste para segunda função
media_final = calcular_media(lista)
print(media_final)

# Teste para terceira função

situacaoAluno = classificar_aluno(lista)
print(situacaoAluno)

# %%

# Melhorando a estrutura de função dentro de outra


def solicitarValores():
    user_notas = []
    
    for i in range(5):
        valor = float(input("Digite uma nota: "))
        user_notas.append(valor)
    return user_notas
    

def calcular_media():
    listaNotas = solicitarValores()
    media = sum(listaNotas) / len(listaNotas)
    return media

def classificar_aluno():
    media = calcular_media()
    
    if media >= 7:
        return 'Aluno aprovado'
    elif media >= 5:
        return 'Aluno de exame'
    else:
        return 'Aluno reprovado'

print('Situação: ',classificar_aluno())

# %%
"""Crie uma função para solicitar 5 notas para o aluno 1, 5 notas para o aluno2.
Em seguida, crie uma estrutura para calcular  a média dos dois alunos.
Por fim, crie uma estrutura para mostrar a situação dos dois alunos"""


def solicitarNotas():
    aluno1 = []
    aluno2 = []
    
    for i in range(5):
        nota1 = float(input('Digite as notas do primeiro aluno: '))
        aluno1.append(nota1)
    for i in range(5):
        nota2 = float(input('Digite as notas do segundo aluno: '))
        aluno2.append(nota2)
        
    return aluno1, aluno2


def media_individuo():
    notas_alunos = solicitarNotas()
    media1 = sum(notas_alunos[0])/len(notas_alunos[0])
    media2 = sum(notas_alunos[1])/len(notas_alunos[1])
    return media1, media2

def situacao_aluno():
    medias = media_individuo()
    media_aluno1 = (medias[0])
    media_aluno2 = (medias[1])
    
    
    if media_aluno1 >= 7:
        return 'Aluno aprovado'
    elif media_aluno1 >= 5:
        return 'Aluno de exame'
    elif media_aluno1 < 5:
        return 'Aluno reprovado'
    
    if media_aluno2 > 7:
        return 'Aluno 2 aprovado'
    elif media_aluno2 >= 5:
        return 'Aluno de exame'
    elif media_aluno2 < 5:
        return 'Aluno reprovado'
    return situacaoAlunos
   
situacaoAlunos = situacao_aluno()
print(situacaoAlunos)


# %%
# Melhorando exercício 2

# Função solicitar os valores
def solicita_valores():
    listaNotas1 = []
    listaNotas2 = []
    
    for i in range(5):
        nota1 = float(input('Digite as notas do primeiro aluno: '))
        listaNotas1.append(nota1)
    for i in range(5):
        nota2 = float(input('Digite as notas do segundo aluno: '))
        listaNotas2.append(nota2)
        
    return listaNotas1, listaNotas2

# Função calcula media

def calcula_media():
    listaNotas1, listaNotas2 = solicita_valores()
    media_aluno1 = sum(listaNotas1) / len(listaNotas1)
    media_aluno2 = sum(listaNotas2) / len(listaNotas2)

    return media_aluno1, media_aluno2

# Função situação  dos alunos

def obter_situacao(media):
    if media >= 7:
        return 'aprovado'
    elif media >= 5:
        return 'de exame'
    else:
        return 'reprovado'

def situacao_aluno():
    medias = calcula_media()
    situacao_aluno1 = f'Aluno 1 {obter_situacao(medias[0])}'
    situacao_aluno2 = f'Aluno 2 {obter_situacao(medias[1])}'
    return situacao_aluno1, situacao_aluno2
    

situacao_aluno()

# %%

# Exemplo multiplicando números

def multiplica(a, b):
    mult = a * b
    return mult

# Multiplicar listas
def multiplicar_lista(lista1, lista2):
    produtos = []
    for i in range(len(lista1)):
        produtos.append(multiplica(lista1[i], lista2[i]))
    return produtos

lista_a = [1, 2, 3, 4, 5]
lista_b = [6, 7, 8, 9, 10]

print(multiplicar_lista(lista_a, lista_b))
    
# %%

"""Crie uma função para solicitar 3 valores para duas listas, chamadas 
lista 1 e lista 2. Ou seja, a lista 1 e 2 devem conter conter 3 valores.

E em seguida crie uma função para elevar ao quadrado (a**2),
multiplicar a * b e apresente os dois resultados em duas listaas diferentes"""

# Importando propiedade para multiplicação de uma lista
from math import prod

# Função para definir os valores da lista
def valores_lista():
    lista1 = []
    lista2 = []
    
    for i in range(3):
        valor1 = int(input('Digite o primeiro valor: '))
        lista1.append(valor1)
    for i in range(3):
        valor2 = int(input('Digite o segundo valor: '))
        lista2.append(valor2)

    return lista1, lista2

# Função para elevar ao quadrado cada elemento individualmente da lista

def indice_ao_quadrado():
    lista1, lista2 = valores_lista()
    resultado_lista1 = []
    resultado_lista2 = []
    
    for i in range(len(lista1)):
        resultado_lista1.append(lista1[i]**2)
        resultado_lista2.append(lista2[i]**2)
    return resultado_lista1, resultado_lista2

# Função para multiplicar os resultados de cada lista

def multiplicacao_quadrado():
    lista1, lista2 = indice_ao_quadrado()
    mult_lista1 = []
    mult_lista2 = []

    for i in range(len(lista1)):
        mult_lista1.append(prod(lista1))
        mult_lista2.append(prod(lista2))
    return mult_lista1, mult_lista2

lista1, lista2 = multiplicacao_quadrado()

print(f'O valor da primeira lista é {lista1[0]}')
print(f'O valor da segunda lista é {lista2[1]}')






