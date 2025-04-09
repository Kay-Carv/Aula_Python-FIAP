"""
Avaliação de Python - FIAP - 09/04/2025
Prof° Francisco                
Nome: Kayque Carvalho
"""

# %%
"""
1.Crie um programa que receba a nota de um aluno (de 0 a 10) e classifique a performance dele conforme os seguintes critérios:
Se a nota for 10, a mensagem será "Nota perfeita!"
Se a nota for de 7 a 9, a mensagem será "Boa nota!"
Se a nota for de 5 a 6, a mensagem será "Nota regular."
Se a nota for abaixo de 5, a mensagem será "Nota baixa." 
"""

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
        print("Opção inválida")

        # %%

"""
4.Crie um programa que recebe o cargo de um funcionário e retorna a faixa salarial correspondente. Utilize a estrutura match case para implementar a lógica:
Se o cargo for "CEO", a faixa salarial será "Acima de 100k."
Se o cargo for "Gerente", a faixa salarial será "Entre 50k e 100k."
Se o cargo for "Analista", a faixa salarial será "Entre 30k e 50k."
Se o cargo for "Estagiário", a faixa salarial será "Menos de 30k."
Caso o cargo não esteja na lista, exiba "Cargo não encontrado."
"""

cargo = str(input("Digite o cargo do funcionário: ")).lower()

match cargo:
    case "ceo":
      print(f"A faixa salarial do cargo de {cargo.upper()} é acima de 100 mil reais")
    
    case "gerente":
      print(f"A faixa salarial do cargo de {cargo.capitalize()} fica entre 50 a 100 mil reais")
    
    case "analista":  
      print(f"A faixa salarial do cargo de {cargo.capitalize()} fica entre 30 a 50 mil reais")
    
    case "estagiario":
      print(f"A faixa salarial do cargo de {cargo.capitalize()} fica abaixo dos 30mil reais")
    
    case _:
      print("Cargo não encontrado")

# %%
"""
5. Crie um programa que recebe informações nas colunas de temperatura, processo e velocidade de operação e retorne a média entre temperatura e processo em uma nova coluna chamada média,
além da classificação da rotação com base na velocidade. 
Utilize uma estrutura para classificar a rotação da seguinte forma:

Se a velocidade for entre 1000 e 1099, a rotação será "Baixa".
Se a velocidade for entre 1100 e 1199, a rotação será "Média".
Se a velocidade for entre 1200 e 1299, a rotação será "Média/Alta".
Se a velocidade for acima de 1300, a rotação será "Alta".

O programa deve gerar um DataFrame com os dados originais, a média entre temperatura e processo, e a classificação da rotação.

"""

import pandas as pd
 
dados = {
     'temperatura': [25, 28, 32, 24, 39] ,
     'processo': [10,12,10,15,18],
     'velocidade': [1000, 1100, 1200, 1200, 1400]
}

df = pd.DataFrame(dados)

for index, row in df.iterrows():
  df.at[index, 'media'] = (row['temperatura'] + row['processo']) /2
  
for index, row in df.iterrows():
  if 1000 <= row['velocidade'] < 1100:
    df.at[index, 'Rotacao'] = 'Baixa'
  elif 1100 <= row['velocidade'] < 1200:
    df.at[index, 'Rotacao'] = 'Media'
  elif 1200 <= row['velocidade'] < 1300:
    df.at[index, 'Rotacao'] = 'Media/alta'
  elif row['velocidade'] > 1300:
    df.at[index, 'Rotacao'] = 'Alta'
 
df
print(df)