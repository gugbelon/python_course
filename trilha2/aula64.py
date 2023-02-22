
from random import( random,
                    uniform,
                    randint,
                    choice,
                    shuffle)
"""
numero = random()
print(numero)
"""


#usando uniform para gerar cinco números aleatórios com uniform
#ele vai de 0 a 1000 e o output sai em decimal e ele nunca chega no limite maximo
"""
for i in range (1,6):
    print(uniform(0,1000))
"""

# randint gera um número aleatório inteiro neste caso de 1 a 100

"""for i in range (1,6):
    print(randint(1,100))
"""

# serve para qualquer estrutura de dados
"""
lista_jokenpo = ["pedra", "papel ","tesoura"]
print(choice(lista_jokenpo))
"""
'''

# embaralha a lista. (tem que ser mutavel a lista que vamos aplicar o shuffle.)
lista = [1,2,3,4,5,6,7,8,9,9,87,546,51,32,165,87,98]
print(lista)
shuffle(lista)
print(lista)
'''