# -*- coding: utf-8 -*-
"""
Python 16/04/2025
Kayque CarvaLho

Estrutura de DataFrame com lambda e dicionário

IDE: spyder
"""
# -----Ex 1-----
soma = lambda x, y: x + y
print(soma(5,5))

# -----Ex 2-----
dobro = lambda z: z*2
print(dobro(10))


# -----Ex 3-----
import pandas as pd

dados = {
    'nome': ['ana', 'bruno', 'carlos'],
    'idade': [25, 30, 22],
    'cidade': ['SP', 'RJ', 'BH']
}

df = pd.DataFrame(dados)

# acessa as informações da coluna idade e altera os valores por meio do aplly e do lambda em + 5, cada uma das linhas da coluna
# apply é como se fosse um for, lambda é uma função rápida
# esse criar nova coluna com dados tratados, é engenharia de recursos, por ex uma coluna que mostra a média de outras duas colunas
df['Idade_mais'] = df['idade'].apply(lambda k: k+5)

df


# -----Ex 4-----

df = pd.DataFrame({'valores': [1,2,3,4,5]})

# criando nova coluna com os valores multiplicados por dois
print(df['valores'].apply(lambda j: j*2))
df['novos_valores'] = df['valores'].apply(lambda j: j*2)
# df['novos_valores'] = df['valores'] * 2  # Evita o uso de lambda para algo simples


# se o valor for divisivel por 2 sera par, se nao sera impar
# apply tem a função de um for, e é bem melhor usar isso pq o codigo fica reduzido
# porém, tem que avaliar se realmente é bom utilizar tais estruturas, ver se nao tem uma melhor e quais as necessidades
df['par_ou_impar'] = df['valores'].apply(lambda x: 'par' if x%2 == 0 else 'impar')

print(df)

df1 = pd.DataFrame({'valores': [1, 2, 3, 4, 5]})
# df1['novos_valores'] = df1['valores'].apply(lambda z:z*2)
df1['novos_valores'] = df1['valores'] * 2

print(df1)

# -----Ex. 6-----

# Dicionário com nomes
dados2 = {
    'nome': ['aNa', 'BruNo', 'FranCisco']
    }

# Atribuindo dados ao dataframe
df2 = pd.DataFrame(dados2)

print(df2['nome'].apply(lambda nome: nome.upper())) # Função para deixar todos os nomes em maiusculos
print(df2['nome'].apply(lambda nome: nome.lower()))
print(df2['nome'].apply(lambda nome: nome.capitalize()))

# -----Ex 8-----

# Um exemplo (talvez não muito prático) de como usar lambda e dataframe para mensurar faixa etária de pessoas
dados3 = {
    'idade': [25, 30, 22, 34, 23, 65]
 }

df3 = pd.DataFrame(dados3)

# df3['faixa_etária'] = df3['idade'].apply(lambda x: 'adulto' if 'idade' <= 25 else 'idoso')
df3['faixa_etária'] = df3['idade'].apply(lambda i: 'adolecente' if i < 18 else 'adulto' if i <60 else 'idoso')

print(df3) 