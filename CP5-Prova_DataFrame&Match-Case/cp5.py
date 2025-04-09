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