# -*- coding: utf-8 -*-
"""
Teste de programação orientada a objetos


"""

# Defiindo atributos de classe para o cachorro
class Cachorro:
    def __init__(self, nome, comida, sono, feliz):
        self.nome = nome
        self.comida = comida
        self.sono = sono
        self.feliz = feliz
        
    def comer(self):
        self.comida -= 1
        
    def dormir(self):
        self.sono = False
        
    def carinho(self):
        self.feliz += 1

"""Uma das principais vantagens é justamente a reutilização do programa acima para podere criar
vários cachorros da classe Cachorro"""
# Nesse caso o nosso objeto seria o cachorro_1 e 2
cachorro_1 = Cachorro("Spyder", 3, False, 8)
cachorro_2 = Cachorro("Jeremias", 1, True, 4)

# Chamando funções como se fossem parte da nossa variável

cachorro_1.comer()
cachorro_2.dormir()

for i in range(5):
    cachorro_2.carinho()