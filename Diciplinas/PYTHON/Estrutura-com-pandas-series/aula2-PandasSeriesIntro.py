# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 08:14:04 2025
FIAP - Engenharia de software
Profº Francisco
IDE utilizada = Spyder

    Esse código foi baseado na aula de Computational Thinking with Python com
o Profº Francisco que tive dentro da Faculdade FIAP no curso de engenharia de software

->Conteúdo da aula<-
Estrutura com pandas series (unidimensional e bidimensional)
- Estrutura de condição
- Estrutura de repetição
- Estrutura de condição dentro de repetição
- Estrutura indexada com pandas series
"""

"""
Pandas Series
->Biblioteca do python - Importe usandado 'import pandas as pd'
    ->Estrutura onde se pode usar a lista e dicionário para organizar os dados
    
    Para estruturar dados gigantes
        ->Como deixar o dado estruturado para o cientistas
"""
"""
Sobre a área de ciencistas de dados 
    ->falando sobre entregas de projetos
    O professor citou alguns exeplos da antiga empresa onde ele trabalhou onde se fazia 
    entregas por sprints dos problemas em que eles iriam resolver as dores dos clientes internos
        ->Citou a importância de seguir etapas e de também
"""
"""
Algumas anotações de código

->case=False-<
comentario.str.caontains('seleção', case=False)      
#O metodo case=False é para fazer com que a busca traga o resultado idependente se for com letras minusculas ou maiusculas

->.empty<-
if not comentarios_filtrados.empty:                         #O atributo .empty verifica se está vazio em Series
    print("\nOs comentários que contêm essa palavra são:")  #False se há pelo menos um elemento presente.
else:
    print("\nNenhum comentário contém essa palavra.")       #True se o objeto está vazio (não há linhas ou valores).
    
->.index<-
O .index serve para mostrar a posição dos elementos (indice) de uma lista por exemplo. Como estou imporatando a biblioteca do
pandas é comum o console trazer o valor do indice no começo de cada elemento, então nesse caso é recomentado deixar .index = False
para não mostrar na hora de printar

comentarios = (['valor 1',
                'valor 2',
                'valor 3',
                'valor 4'])
print(comentarios.to_string(index=False))

->\n<-
O /n no começo do print serve para quebrar o texto a cada linha
print("Linha 1")
print("\nLinha 2")


"""
# %%
# Imporatndo bilbioteca externa do pandas

import pandas as pd
pd.DataFrame({'A': [1, 2, 3]})

a = 1
print(a)

# %%

#Exemplo 1 

numero = int(input("Digite um númrero: "))
numeros = []
 
for k in range(5):
        
    num = float(input("Digite um valor para a lista: "))
    numeros.append(num)
    
print("Os respequitivos valores são: ", numeros)

for i in range(len(numeros)):
    if numeros[i] == 30:
        print(f"A posição do número está em : {i}")
        break

# %%
"""
1. Crie uma estrutura em python para solicitar a quantidade de pessoas que podem fazer comentários sobre
um post, em seguida, crie a estrutura para o usuário inserir a informação. Em seguida, crie a estrutura
para verificar a posição a qual um alvo está dentro da lista

Passos:
    - Estrutura de entrada para definir a quantidade de pessoas que poderão fazer 
    comentários fazer os comentários
    
    - Definir um alvo para o problema
    alvo = 'gol'
    
    - Estrutura de condição dentro de repetição para verificar o alvo dentro da lista
"""


pessoas = int(input("Defina a quantidade de pessoas que podem fazer comentários: "))
alvos = []

for k in range(pessoas):
    
    com = str(input("Digite o comentário de cada pessoa: "))
    alvos.append(com)

alvo = 'gol'
for i in range(len(alvos)):
    if alvos[i] == alvo:
        i = i + 1
        print(f" O comentário {i} contém o alvo "f"{alvo}")
        
#       break    OBS: Se 

# %%

import pandas as pd

pd_series = pd.Series([10, 20, 30, 40, 50]) #O spyder mostra o tipo de forma diferente

print(pd_series)

s1 = pd.Series([10, 20, 30, 40, 50])
s2 = pd.Series([1, 2, 3, 4, 5])

#Operações matemáticas no pandas Series

soma = s1 + s2
print(soma)

mult = s1 * s2
print(mult)

sub = s1 - s2
print(sub)

div = s1 / s2
print(div)


# %%

import pandas as pd

#Nomeando as listas      //Semelhante a dar nome nas colunas do excel
s1 = pd.Series([10, 20, 30, 40, 50], name='Serie1')
s2 = pd.Series([1, 2, 3, 4, 5], name= 'Serie2')
print(s1)
print(s2)

#Dicionário

# ESTRUTURA UNIBMENCIONAL
data = { 'A': [1, 2, 3],
         'B': [4, 5, 6],
         'C': [7, 8, 9]}
print(data)

#Transformando dicionário em linha e colunas usando pandas

# ESTRUTURA BIDIMENCIONAL
data_frame = pd.DataFrame(data)
print(data_frame)

#Criar range de valores dizendo de onde incia e onde termina

s = pd.Series(range(1, 11))
print(s)

print(s[3])

# %%

import pandas as pd

s1 = pd.Series([10, 20, 30, 40, 50])

k = 0

while k < len(s1):
    print(f"O índice: {k}")
    k += 1

for g in s1:
    
    if g > 30:
        print(f"O valor {k} é maior do que 30")
    else:
        print(f"O valor de e{g} é menor do que 30")
# %%
import pandas as pd

#ALGUMAS FUNÇÕES DO PANDAS

letras = pd.Series(['ana', 'bianca', 'cecilia', 'denise', 'eeugenio'])

print(letras.iloc[2])
print(letras.iloc[:2])
print(letras.iloc[-2:])

print(letras.str.upper())    #deixa em maiusculo

letras1 = pd.Series(['AnA', 'BIancA', 'CeciliA'])
print(letras1.str.lower())   #Deixa em mminusculo

nomes = pd.Series(['ana silva',
                   'bianca de jesus',
                   'cecilia bezerra',
                   'denise souaz',
                   'eugenio junior'])

print(nomes.str.split().str[1])         #Pega apenas a segunda palavra dentro de string

emails = pd.Series(['ana@hotmail.com',
                   'bianca@gmail.com',
                   'carol@fiap.com'])

#Verificar padrões

filtro_email = (emails[emails.str.endswith("@hotmail.com")])    #Traz apenas os email que terminam com essa nomenclatura
print(filtro_email)

contem_nomes = (emails[emails.str.contains('carol')])     #Traz os emails que contém essa string
print(contem_nomes)

substituicao_email = emails.str.replace('hotmail.com', 'gmail.com')  #Substitui uma str pela outra
print(substituicao_email)

#Frases
#Contar palavras dentro de frases

frases = pd.Series([
    "python é uma linguagem muito usada",
    "Hoje está muito quente",
    "Hoje é quinta feira de aula com python",
    ])

print(frases)

contar = frases.str.contains("python").sum()  #Soma a quantidade de vezes que a palvra aparece entre as frases do tipo string

# %%

"Exercicios"
import pandas as pd

# 1. Para as três series do pandas chamada de s1, s2 e s3. Resolva as sequintes operações
s1 = pd.Series([1.5, 2.5, 3.5, 4.5, 5.5])
s2 = pd.Series([1, 2, 3, 4, 5])
s3 = pd.Series([5, 10, 15, 20, 25])
# a) s1 + s2
soma = s1 + s2
print(soma)

# b) (s1 + s3) * s2
somaB = (s1 + s3)
resultB = somaB * 2
print(resultB)

# c) (s3 - s2) * s1
subC = s3 - s2
resultC = subC * s1
print(subC)
print(resultC)

# d) s3 * s2 a* s1

multD = s3 * s2 * s1
print(multD)

# %%
import pandas as pd

# 2. Dado uma série relacionada a distância em km com as sequintes informações: 10, 5, 2, 15, 8.
# Consideranado que o primeiro valor é o primeiro  dia e o úlltimo valor é o útimo dia, reponda:

# a) Qual a distância percorrida no primeiro e último dia?
km = pd.Series([10, 5, 2, 15, 8])

print(f"No primeiro dia foi percorrido {km.iloc()[0]}km!")
print(f"No ultimo dia foi percorrido {km.iloc()[-1]}km!")      #Nesse caso, para pegar o utltimo indice a gente coloca [-1], já que o indice sempre começa em 0

# b) Qual a distância total percorrida?
soma = sum(km)
print(soma)

# c) Qual a distância média?
media = soma / len(km)
print(int(media))

# 3. Pensando no problema que envolve a análise de comentários sobre o Neymar. 
# Crie uma estrutura para analisar os comentários feitos pelos usuários e dizer quantos posts estão 
# falando sobre gol, seleção, santos.

comentario = pd.Series(["Que gol lindo do Neymar na seleção!",                    
                        "Ele deveria voltar para a seLeção depois desse gol.", 
                        "O santos revelou grandes craques como Neymar.",
                        "O último gol do Neymar foi um gol olimpico! Que emoção!!!", 
                        "A seleção brasileira precisa dele!",
                        "Fiquei muito feliz com a volta do Neymar pro Santos"])

#Soma a quantidade de comentários com essas palavras
contem_Santos = comentario.str.contains('Santos', case=False).sum()
contem_selecao = comentario.str.contains('seleção', case=False).sum()      #O metodo case=False é para fazer com que a busca traga o resultado idependente se for com letras minusculas ou maiusculas
contem_gol = comentario.str.contains('gol', case=False).sum()

print(f"Tiveram {contem_Santos} comentário(s) com a palavra 'Santos'.")
print(f"Tiveram {contem_selecao} comentário(s) com a palavra 'seleção'.")
print(f"Tiveram {contem_gol} comentário(s) com a palavra 'gol'.")

#Fala em quais comentários apareceram as palavras

comentario_Santos = (comentario[comentario.str.contains('Santos', case=False)])
comentario_selecao = (comentario[comentario.str.contains('seleção', case=False)])
comentario_gol = (comentario[comentario.str.contains('gol', case=False)])

print( "A palavra santos aparece nos seguintes comentários:")
print(comentario_Santos)

print( "A palavra 'seleção' aparece nos seguintes comentários:")
print(comentario_selecao)

print( "A palavra 'gol' aparece nos seguintes comentários:")
print(comentario_gol)

# %%

import pandas as pd

'''Solicitando ao usuário para inserir qual palavra ele deseja encontrar nos comentários'''

comentarios = pd.Series(["Que gol lindo do Neymar na seleção!",                    
                        "Ele deveria voltar para a seLeção depois desse gol.", 
                        "O santos revelou grandes craques como Neymar.",
                        "O último gol do Neymar foi um gol olimpico! Que emoção!!!", 
                        "A seleção brasileira precisa dele!",
                        "Fiquei muito feliz com a volta do Neymar pro Santos"])

palavra = input("Digite uma palavra para achar nos comentários: ")

input_palavra = comentarios.str.contains( palavra, case=False)

print(f"Tiveram {input_palavra.sum()} comentário(s) com a palavra '{palavra}'")


# %%
# Adicionando estrutura de condição e comentários no código

import pandas as pd

'''Solicitando ao usuário para inserir qual palavra ele deseja encontrar nos comentários'''

comentarios = pd.Series([
    "Que gol lindo do Neymar na seleção!",                    
    "Ele deveria voltar para a seLeção depois desse gol.", 
    "O santos revelou grandes craques como Neymar.",
    "O último gol do Neymar foi um gol olimpico! Que emoção!!!", 
    "A seleção brasileira precisa dele!",
    "Fiquei muito feliz com a volta do Neymar pro Santos"
])

# Solicita a palavra ao usuário
palavra = input("Digite uma palavra para achar nos comentários: ")

# Verifica quais comentários contêm a palavra que o usuário inseriu
input_palavra = comentarios.str.contains(palavra, case=False)

# Exibe os resultados
print(f"\nTiveram {input_palavra.sum()} comentário(s) com a palavra '{palavra}'.")      #/n serve para quebrar a linha entre um print e outro
comentarios_filtrados = comentarios[input_palavra]

# Estrutura de condição
if not comentarios_filtrados.empty:                         #O atributo .empty verifica se está vazio em Series
    print("\nOs comentários que contêm essa palavra são:")  #False se há pelo menos um elemento presente.
    print(comentarios_filtrados.to_string(index=False)) #.to_string(index=False), serve para tirar o indice que aparece no terminal na hora de printar
else:
    print("\nNenhum comentário contém essa palavra.")       #True se o objeto está vazio (não há linhas ou valores).




















