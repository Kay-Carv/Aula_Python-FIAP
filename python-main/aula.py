# %% 
# EX 1: Estrutura de repetição com DataFrame
import pandas as pd

# Criando um DataFrame simples
dados = {
    "Nome": ['ana', 'brono', 'carlos'],
    "Idade": [25, 30, 22],
    "Cidade": ['SP', 'RJ', 'BH']
}

df = pd.DataFrame(dados)

# Iterando pelas linhas e exibindo nome e idade
for indice, linha in df.iterrows():
    print(f"Índice: {indice}, Nome: {linha['Nome']}, Idade: {linha['Idade']}")

# %%
# EX 2: Cálculo da média de notas com correção no cálculo

dados = {
    'Aluno': ['joão', 'maria', 'pedro'],
    'Nota1': [7.5, 8.0, 6.5],
    'Nota2': [8.0, 9.0, 7.0],
}
df1 = pd.DataFrame(dados)

# Cálculo correto da média
for indice, linha in df1.iterrows():
    media = (linha["Nota1"] + linha["Nota2"]) / 2
    print(f"{linha['Aluno']} tem média {media:.1f}")

# %%
# EX 3: Adicionar nova coluna com idade incrementada

dados = {
    "Nome": ['ana', 'brono', 'carlos'],
    "Idade": [25, 30, 22],
    "Cidade": ['SP', 'RJ', 'BH']
}

df = pd.DataFrame(dados)

# Criando uma nova coluna com a idade somada de 1 ano
df['Idade_Nova'] = df['Idade'] + 1
print(df)

# %%
# EX 4: Estrutura de repetição com while para buscar por nome

indice = 0
encontrou = False

while indice < len(df) and not encontrou:
    if df.loc[indice, "Nome"] == 'bruno':
        print(f"Bruno encontrado no índice {indice}")
        encontrou = True
    indice += 1

# %%
# EX 5: Uso da função apply para deixar os nomes em maiúsculo

df['Nome1'] = df['Nome'].apply(lambda x: x.upper())
print(df)

# %%
# EX 6: Aplicar desconto aos produtos usando função

dados = {
    "Produto": ['caneta', 'caderno', 'livro'],
    "Preço": [5, 30, 45],
}

df_prod = pd.DataFrame(dados)

# Função para aplicar 10% de desconto
def aplica_desconto(preco):
    desconto = preco * 0.9
    return desconto

# Aplicar a função e criar nova coluna
df_prod['Preço com Desconto'] = df_prod['Preço'].apply(aplica_desconto)
print(df_prod)

# %%
# EX 7: Importar CSV e realizar cálculos estatísticos

import pandas as pd

# OBSERVAÇÃO: Lembra de substituir pelo caminho correto do arquivo
df = pd.read_csv('/content/manutencao_preditiva.csv')

# Cálculos estatísticos sobre a coluna 'Temperatura Ar [K]'
print("Temperatura Ar [K]")
print("Mínimo:", df['Temperatura Ar [K]'].min())
print("Máximo:", df['Temperatura Ar [K]'].max())
print("Média:", df['Temperatura Ar [K]'].mean())
print("Mediana:", df['Temperatura Ar [K]'].median())

# %%
# EX 8: Gráfico usando matplotlib

import matplotlib.pyplot as plt

# Definindo variáveis do gráfico
x = df['UDI']
y = df['Temperatura Ar [K]']
y2 = df['Temperatura Processo [K]']  # Certifique-se de que essa coluna existe

# Criando o gráfico
plt.plot(x, y, label='Temperatura do Ar')
plt.plot(x, y2, label='Temperatura do Processo')
plt.xlabel('UDI')
plt.ylabel('Temperaturas (K)')
plt.legend()
plt.show()

# %%
# EX 9: Categorizar torque com função personalizada

# Função para categorizar torque
def categorizar_torque(torque):
    if torque < 20:
        return 'baixo'
    elif torque < 40:
        return 'medio'
    else:
        return 'alto'

# Aplicar a função à coluna de torque
df['Torque 1'] = df['Torque [Nm]'].apply(categorizar_torque)

# Exibir contagem por categoria
print(df['Torque 1'].value_counts())
