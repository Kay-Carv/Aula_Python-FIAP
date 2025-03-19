# -*- coding: utf-8 -*-
"""
20/02/2025

Aula de listas e tuplas
Prof. Dr. Francisco
IDE = Spyder 

Tema da aula: Tuplas 

Check point = Tema: Tuplas e estrutura de repetição com tuplas

obs: Listar para inserir é mais lenta
"""
"""Conteúdo da aula---

Tupla = (     )    Obs:  Diferente da lista ela é imutavel
lista = [     ]
lista bidimencional [ [], [], []]      Array com várias listas/Matriz
 = ( [( ), ( )], ( ), [(), ( ), ( )])
-----------------------
Repertório
Dbeaver = Trabalhar com SQL tmb permite conectar e manipular vários bancos de dados
    ->Usado para engenharia de dados

Indice = Dentro de lista ou tuplas seria a posição de um elemento dentro dela
    Ex:  [1, 2, 4, ]
    Indice 0 da lista = 1
    Indice 2 da lista = 4

tuple = Transforma uma lista em tupla e/ou Separa os caracteries de um string
"""
# %%
# Conteúdo para próxima semana
#Exemplo de matriz usando dicionário
matriz_dicionario = {
    (0, 0): 1, (0, 1): 2, (0, 2): 3,
    (1, 0): 4, (1, 1): 5, (1, 2): 6,
    (2, 0): 7, (2, 1): 8, (2, 2): 9
}

# Acessando um elemento
print(matriz_dicionario[(0, 1)])


# %%
#Exemplos

lista_numeros = [1, 2, 3, 4]
print(lista_numeros)

tupla_numeros = (1, 2, 3, 4)
print(tupla_numeros)

lista_bidimencional = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lista_bidimencional)

# %%

#-->Exemplo de tupla<--

tupla = 4, 5, 6   #O Py entende commo tupla mesmo sem estar dentro dos parenteses
print(tupla)

primeira_posicao = tupla[0]
print(primeira_posicao)

segunda_posicao = tupla[1]
print(segunda_posicao)

terceira_posicao = tupla[2]
print(terceira_posicao)

#Tupla dentro de uma tupla

tupla_tupla = ((4, 5, 6), (7, 8))
print(tupla_tupla)


#-->Exemplo de lista<--

lista = [4, 5, 6]
print(lista)

primeira_posicao_lista = [0]   #Defini o indice da lista para depois printar o valor respectivo a esse indice
print(primeira_posicao_lista)

# %%
#Tupla dentro de uma tupla

tupla_tupla = ((4, 5, 6), (7, 8))
print(tupla_tupla)

posicao1 = tupla_tupla[0]
print(posicao1)


#Posição dentro de outra
posicao2 = tupla_tupla[1][1]    #Vai trazer o número 8
print(posicao2)

posicao3 = tupla_tupla[0][1]
print(posicao3)

posicao4 = tupla_tupla[0][2]
print(posicao4)

# %%

#Tuplas com strings

tupla_letra = ('a', 'b', 'c' )
print(tupla_letra)


tupla_universidades = ('fiap', 'USP', 'Unicamp')
print(tupla_universidades)


tupla_tupla_str = (('a', 'b', 'c' ), ('fiap', 'USP', 'Unicamp'))
print(tupla_tupla_str)

#Função tuple = Separar os caracteries de ma string
tupla = tuple('FIAP')
print(tupla)

tupla1 = tuple('Separando os caracteres')
print(tupla1)


#Lista

lista_universidades = ['fiap', 'USP', 'Unicamp']
print(lista_universidades)

# %%

#Tuplas com variaveis de diferentes tipos

tupla = tuple(['foo', [1,1], True])
print(tupla)

posicao2 = tupla[2]
print(posicao2)

#tupla[2] = True  ##Aqui temos um erro por a tupla não permitir trocar a informação
#print(tupla[2])

# %%

tupla = tuple(['foo',[1,1], True])
print(tupla)

#Converte tupla em lista para que ela seja mutavel
lista = list(tupla)
print(lista)

lista.insert(0, 'hoje')  #Transformando o indice 0 no objeto str 'hoje'
#lista_nova = lista.insert(0, 'hoje')
nova_tupla = tuple(lista)
print(nova_tupla)

# %%

# -->Exercício: Inclua a palavra Fiap na posição 1 da nova tupla

tupla = tuple(['foo',[1,1], True])
print(tupla)

#Converte tupla em lista para que ela seja mutavel
lista = list(tupla)
print(lista)

lista.insert(0, 'hoje')  #Transformando o indice 0 no objeto str 'hoje'
lista.insert(1, 'Fiap')

#Converte lista em tupla novamente
nova_tupla = tuple(lista)
print(nova_tupla)

# %%


tupla = tuple(['foo',[1,1], True])

lista_mutavel = list(tupla)         #Converte tupla em lista

lista_mutavel.insert(3, 'Alou alou')

palavra = input("Digite aqui um palavra para ser adicionada no indice 2:   ")

lista_mutavel.insert(2, palavra)

print(lista_mutavel)

# %%

tupla = tuple(['foo',[1,1], True])
lista = list(tupla)

# ".index( )" é a referência e o número significa quantas posições a informação será inserida
posicao_insercao = lista.index([1,1]) + 1   

nova_tupla = tuple(lista)
print(nova_tupla)

# %%

#Ex :
'A partir da palavra foo, insira a palavra fiap 2 posições para frente e a palavra usp 1 posição para frente'

tupla = tuple(['foo',[1,1], True])

lista = list(tupla)

duas_posicoes_insercao = lista.index('foo') + 1
lista.insert(duas_posicoes_insercao, 'USP')

duas_posicoes_insercao = lista.index('foo') + 2
lista.insert(duas_posicoes_insercao, 'FIAP')

print(lista)

# %%

#Operações com tuplas

#Concatena as informações
operacao_soma = (4, None, 'foo') + (6, 0) + ('bar', 1)
print(operacao_soma)

#Repete e informação 4 vezes
mult = ('foo', 'bar') * 4
print(mult)

#Concatena as informações
soma = (4, 8, 12) + (3, 6, 9)
print(soma)

# %%
#Descompactando a tupla

tupla = (4, 5, 6)
print(tupla)
a, c, b = tupla  #o py permite a gente ver os elementos dessa forma (Pode ser definido por qualquer palavra no lugar dessas letras)
print(a)
print(b)
print(c)


tupla1 = 4, 6, (6, 7)   #Vira uma única tupla
print(tupla1)

#Desmembrando a tupla
a, b, (c, d) = tupla1
print(a)
print(b)
print(c)
print(d)

a, b = 1, 2
a, b = b, a

print(a)
print(b)
#%%
# Selecionando um elemento específico na tupla

frutas = ('maça', 'banana', 'laranja', 'uva')

#Mostra apenas os dados a qual deseja selecionar a partir do indice...
frutas_modificadas = frutas[:1] # Exibe a informação desejada
print(frutas_modificadas)


frutas_modificadas = frutas[2:]  #Não mostra a informação antes
print(frutas_modificadas)
#Mostra apenas os dados a qual deseja se



# %%

# ---> ESTRUTURA DE REPETIÇÃO COM TUPLA <---

'Obs: Use o python tutor para verificar a lógica do código'

tupla = (4, 8, 12)

for i in tupla:
    novo_numero = i * 2
    print(i)
# %%

# ---> ESTRUTURA DE REPETIÇÃO COM TUPLA <---

'Obs: Use o python tutor para verificar a lógica do código'

tupla = (4, 8, 12)
nova_tupla = []

for i in tupla:
    novo_numero = i * 2
    nova_tupla.append(novo_numero)    #append para passar a tupla para lista para poder modificar o resultado

tupla_atualizada = tuple(nova_tupla)  #Volta os resultados da lista para a tupla (Tupla é imutavel) 
print(tupla_atualizada)
#print(nova_tupla)

# %%
# 1. Crie uma tupla chamada frutas com os seguintes elementos: 'maça', 'banana', 'laranja', 'uva'
# 2. Mostre apenas a informação da segunda posição da tupla frutas
# 3. Subistitui o terceiro indice por 'manga'
# 4. Crie uma tupla com 'abacaxi' e 'limão' depois some com frutas_motificadas e retorne em
# uma nova tupla chamada frutas_concatenadas

#%%
# EX que eu fiz 

tupla_frutas = 'maça', 'banana', 'laranja', 'uva'  #Lembrando que o py entende como tupla mesmo estando fora dos parenteses

posicao2 = tupla_frutas[1]
print(posicao2)

frutas_motificadas = list(tupla_frutas)

frutas_motificadas.insert(2, 'manga')

print(frutas_motificadas)

tupla = ('abacaxi', 'limão')
lista = list(tupla)

frutas_concatenadas = tuple(frutas_motificadas + lista)

print(frutas_concatenadas)


    
# %% Resolução feita pelo professor

#Ex 1 

frutas = ('maça', 'banana', 'laranja', 'uva')
print(frutas)

#Ex 2

segunda_fruta = frutas[1]
print(segunda_fruta)

#ex 3 - Subistitui o terceiro indice por 'manga'

frutas_modificadas = frutas[:2] + ('manga',) + frutas [3:]
print(frutas_modificadas)

# %%
#Crie uma tupla chamada numeros com os números de 1 a 5

#Multiplique cada elemento da tupla numeros por 2 e armazene o resultado em uma nova tupla chamada numeros_dobrados

#Obs > utilize estrutura de repetição

numeros = (1, 2, 3, 4, 5)
valores_dobrados = []


for i in numeros:
    i = i * 2
    valores_dobrados.append(i)

numeros_dobrados = tuple(valores_dobrados)
print(numeros_dobrados)


