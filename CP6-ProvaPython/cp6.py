"""
FIAP - 21/05/2025
"""

# %%
"""2. Crie um programa que receba a nota de um aluno (de 0 a 10) e classifique a performance dele conforme os seguintes critérios:
Se a nota for 10, a mensagem será "Nota perfeita!"
Se a nota for de 7 a 9, a mensagem será "Boa nota!"
Se a nota for de 5 a 6, a mensagem será "Nota regular."
Se a nota for abaixo de 5, a mensagem será "Nota baixa."

Obs: utilize função def e Implemente essa lógica usando a estrutura match case."""

def notas():
  nota = int(input("Digite a nota de 0 a 10 do aluno: "))
  match nota:
      case int() if 0 <= nota < 5 :
          print("Nota baixa")
      case 5 | 6:
          print("Nota regular")
      case int() if 7 <= nota <= 9:
          print("Boa nota!")
      case 10:
          print("Nota perfeita!")
      case _:
          print("Opção inválida, digite um valor entre 0 a 10")
          notas()

notas()


# %%
"""
3. Crie um programa que recebe o cargo de um funcionário e retorna a faixa salarial correspondente. Utilize a estrutura match case para implementar a lógica:
Se o cargo for "CEO", a faixa salarial será "Acima de 100k."
Se o cargo for "Gerente", a faixa salarial será "Entre 50k e 100k."
Se o cargo for "Analista", a faixa salarial será "Entre 30k e 50k."
Se o cargo for "Estagiário", a faixa salarial será "Menos de 30k."
Caso o cargo não esteja na lista, exiba "Cargo não encontrado."


"""

def cargos():
  cargo = str(input("Digite o cargo do funcionário: ")).lower()

  match cargo:
    case "ceo":
      print(f"A faixa salarial do cargo de {cargo.apply(lambda x: x.upper)} é acima de 100 mil reais")
    
    case "gerente":
      print(f"A faixa salarial do cargo de {cargo.capitalize()} fica entre 50 a 100 mil reais")
    
    case "analista":  
      print(f"A faixa salarial do cargo de {cargo.capitalize()} fica entre 30 a 50 mil reais")
    
    case "estagiario":
      print(f"A faixa salarial do cargo de {cargo.capitalize()} fica abaixo dos 30mil reais")
    
    case _:
      print("Cargo não encontrado, digite um cargo valido!")
      cargos()

cargos()


# %%
def faixa_salarial(cargo):
    cargo = cargo.lower()

    cargos_dict = {
        "ceo": lambda: f"A faixa salarial do cargo de {cargo.upper()} é acima de 100 mil reais",
        "gerente": lambda: f"A faixa salarial do cargo de {cargo.capitalize()} fica entre 50 a 100 mil reais",
        "analista": lambda: f"A faixa salarial do cargo de {cargo.capitalize()} fica entre 30 a 50 mil reais",
        "estagiario": lambda: f"A faixa salarial do cargo de {cargo.capitalize()} fica abaixo dos 30 mil reais"
    }

    #  retorna mensagem padrão (get) ou retorna a stc de acordo com a chave
    return cargos_dict.get(cargo, lambda: "Cargo não encontrado, digite um cargo válido!")()

def cargos():
    cargo_input = input("Digite o cargo do funcionário: ")
    print(faixa_salarial(cargo_input))

cargos()


# %%

""""
4. Crie uma lógica para criar duas novas colunas do dataframe sobre falhas e mostre as respectivas alterações:

1. Calcule a média entre as duas colunas temperatura do ar e processo.2. Crie uma nova coluna a partir dos valores de velocidade de rotação da máquina:  1000 a 1100 - Baixa rotação  1100 a 1200 - Rotação Média
1200 a 1300 - Rotação media/alta
> 1300 - Alta rotação

Obs: Utilize função def e apply para fazer isso.

"""
import pandas as pd

df = pd.DataFrame({
    'temperatura_ar': [30, 45, 50, 40, 35],
    'temperatura_processo': [70, 85, 90, 75, 65],
    'velocidade_rotacao': [1050, 1150, 1250, 1350, 950]
})

# média entre duas colunas
def calcular_media_temp(ar, processo):
    media = (ar + processo) / 2 
    return media

# Cria uma nova coluna com a média
df['media_temperatura'] = calcular_media_temp(df['temperatura_ar'], df['temperatura_processo'])

# Função para classificar a rotação
def classificar_rotacao(rotacao):
    if 1000 <= rotacao < 1100:
        return 'Baixa rotação'
    elif 1100 <= rotacao < 1200:
        return 'Rotação média'
    elif 1200 <= rotacao < 1300:
        return 'Rotação média/alta'
    elif rotacao >= 1300:
        return 'Alta rotação'
    else:
        return 'Rotação fora do padrão'

df['categoria_rotacao'] = df['velocidade_rotacao'].apply(classificar_rotacao)

print(df)


# %%

"""
5. Você recebeu um DataFrame com informações sobre produtos à venda, incluindo o nome do produto, o preço original e a categoria.
Sua tarefa é calcular o preço com desconto com base na categoria do produto:

Categoria "Eletrônico" → 10% de descontoCategoria "Roupas" → 20% de descontoCategoria "Alimento" → 5% de descontoQualquer outra categoria → Sem desconto

Crie uma nova coluna chamada "Preço com Desconto" aplicando uma função def com apply e lambda."""


import pandas as pd

df = pd.DataFrame(
  {
    'Produto': ['Notebook', 'Camisa', 'Arroz', 'Fone de ouvido', 'Livro'],
    'Preco': [3500, 80, 25, 150, 60],
    'Categoria': ['Eletrônico','Roupas', 'Alimento', 'Eletrônico', 'Outros']
  })

# Função de desconto
def aplica_desconto(dados):
    if dados['Categoria'] == 'Eletrônico':
        return dados['Preco'] * 0.9
    elif dados['Categoria'] == 'Roupas':
        return dados['Preco'] * 0.8
    elif dados['Categoria'] == 'Alimento':
        return dados['Preco'] * 0.95
    else:
        return dados['Preco'] 

df['Preço com Desconto'] = df.apply(lambda linha: aplica_desconto(linha), axis=1) # Axis serve para pegar o valor da linha inteira

print(df)