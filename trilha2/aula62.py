# funcao que pega sobrenome 
def pegar_sobrenome():
    #loop while startando com true
    while True:
        # entrada de dados 
        sobrenome = input("Digite seu sobrenome: ")
        # verifica se não é um input vazio
        if sobrenome:
            #aqui e que ele pega o input e ve se o primeiro digito e uma letra
            if sobrenome.isalpha():
                # retorna o sobrenome válido
                return sobrenome
            # caso digite a primeira letra e ela não seja alfabetica ele cai no else
            else:
                print(" Digite um sobrenome valido!!!! ")
            
        else:
            return sobrenome


def pega_idade():
    while True:
        try:
            idade = int(input("Digite a sua idade: "))

        except:
            print("Digite uma idade válida!!! ")
        else:
            if idade:
                return idade
            else:
                print("Digite uma idade válida !!!!! ")


def pega_altura():
    while True:
        try:
            altura = float(input("Digite sua altura: "))
        except:
            print("Você fez caquinha, tente outra vez ")
        else:
            if altura:
                return altura
            else:
                print("Você fez caquinha, tente outra vez ")


def pega_peso():
    while True:
        try:
            peso = float(input("Digite seu peso: "))
        except:
            print("Você fez caquinha, tente outra vez ")
        else:
            if peso:
                return peso
            else:
                print("Você fez caquinha, tente outra vez")


lista_pessoas = []
contador = 0

# gurdando os dados usando while e usando um if para as condições sejam atendidas
while True:
    sobrenome = pegar_sobrenome()
# caso o sobrenome estiver vazio ele cancela o loop    
    if sobrenome:
        contador += 1
        altura = pega_altura()
        idade = pega_idade()
        peso = pega_peso()
        #lista temporaria salvando na ordem que o desafio pede
        lista_temp = [sobrenome, altura, idade, peso]
        lista_pessoas.append(lista_temp)
    #caso não de certo ele da um break
    else:
        break

soma_idade = 0
soma_peso = 0
soma_altura = 0

if contador > 0:
    lista_pessoas.sort()
    print("Relação de nomes cadastrados.....")
    print("=" * 32)

    for i in range(0, len(lista_pessoas)):
        print(
        f'{lista_pessoas[i][0]}\t- {lista_pessoas[i][1]}\t\
- {lista_pessoas[i][2]}\t - {lista_pessoas[i][3]} ')
        soma_idade += lista_pessoas[i][1]
        soma_altura += lista_pessoas[i][2]
        soma_peso += lista_pessoas[i][3]
    print("="* 32)
media_idade = soma_idade/contador
media_peso = soma_peso/contador
media_altura = soma_altura/contador
print(f"Idade média: {round(media_idade,2)}")
print(f"Altura média: {media_altura}")
print(f"Peso médio: {media_peso}")
print('='* 32)
