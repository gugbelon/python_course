"""
try:
   num = int(input("Digite um número: "))

except:
    print("Valor incorreto")
else:
    print(f"o número digitado foi {num}")
    
finally:
    
    print("Fim da execução do programa!!!!")
    
"""
# funcão que pega dois parametros, a e o b
def divisao(a, b):
    """
    Param a: Dividendo da operação
    Param b: Divisor da operação
    Result: Se sucesso, retorna divisão. Caso contrário, raise error
    """

# try e except, tentar retornar a divisao de a e b    
    try:
# retornando a divisão de dois inteiros        
        return int (a) / int(b)
    except(ValueError, ZeroDivisionError)as erro:

# retorna um f strig caso entra no except         
        return f'ocorreu um problema {erro}'
    
# duas variaveis int que recebem input para gerar os dois números que eu preciso.
n1 = int(input('informe o dividendo: '))
n2 = int(input('informe o divisor: '))
divisao()
print( divisao( n1 , n2 ) )

