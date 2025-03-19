# %%
# Ex1

m = float(input("Insira o valor de massa em KG: "))
energia = (m* 3 * pow(10,8))/1000000 #Transformando em megajaules
print("A energia resultante é de:", energia, "Mjoules")

# %%
#Média de notas
nota1 = float(input("Ensira a primeira nota: "))
nota2 = float(input("Ensira a segunda nota: "))
nota3 = float(input("Ensira a terceira nota: "))

lista = [nota1, nota2, nota3]
media = (nota1 + nota2 + nota3)/len(lista)
print("A média das notas é :", media)

# %%
#Estrutura de condição

A = float(input("Digite o valor de A: "))
B = float(input("Digite um valor para B: "))

if A > B:
    print("A é maior que B")
else:
    print("B é maior que A")
# %%
##Ex: 4

idade = int(60)

if idade < 11:
    print("É uma criança")
elif idade >11 < 21:
    print("É um adolecente")
elif idade > 21 < 40:
    print("Adulto-jovem")
elif idade > 40 < 65:
    print('Meia-idade')
elif idade > 65:
    print("Idoso")
else:
    print("É não vey")

# %%
##Ex: 5

velocidade = float(input("Insira o valor da velocidade: "))
pontosCarteira = 15

if  44 >= velocidade < 48:
    pontosCarteira += 3
    print("Infração leve")
elif 48 > velocidade < 50:
    print("Infração média")
    pontosCarteira += 4
elif 52 > velocidade < 60:
    print("Infração grave")
    pontosCarteira += 5
elif velocidade >= 60:
    print("Infração gravissíma")
    pontosCarteira += 7
else:
    print("Nenhuma infração foi cometida")

print("O motorista tem ", pontosCarteira,"ponto(s) na carteira")

if pontosCarteira >= 20:    
    print("Perde a carteira")
else:
    print('Não perde a carteira')
    
#leve: 3 pontos, Infração média: 4 pontos, 
#Infração grave:5 pontos, Infração gravíssima: 7 pontos. 

# %%


infracao = str(input("Qual a infração cometida?"))

if infracao == "Lanterna quebrada" :
    
# %%

possui_habilitacao = input("Possui habilitação? (sim ou não)")

if possui_habilitacao == 'sim':
    carteira_valida = input("O registro está no prazo de validade? (sim ou não)")
    sinistro_carro = input("Digite o tipo de sinistro")

    if carteira_valida == 'não':
        print("Você está inregular e será multado")
    elif sinistro_carro == 'Lanterna quebrada':
        print("Você será multado")
        
else:
    print("carro será apreendido")
    
# %%
#Ex: 7

carros = ['audi', 'bmw', 'subaru', 'toyota']

carro_digitado = str(input("Digite a marca do carro"))

#Verificar se está dentro da lista
if carro_digitado == 'audi';:
    print("O carro escolido é: ", carro_digitado)
    
else:
    print("Carro não está na lsita")

# %%        
#Estrutura de repetição

carros = ['audi', 'bmw', 'subaru', 'toyota']

carro_digitado = str(input("Digite a marca do carro"))

carro_encontrado = False

for carro in carros:
    if carro == carro_digitado:
        carro_encontrado = True
        break
    
if carro_encontrado:
    print(f'O carro digitado é {carro_digitado}')
else:
    print(f'O carro digitado {carro_digitado} não está na lista')
    

