# estanciando funções lambda para gerar outputs de tamanho suma e o numero maximo.
media = lambda seq: len(seq) / sum (seq)
total = lambda seq: sum(seq)
maximo = lambda seq: max(seq)

#Lista de dicionários contendo nome e notas como chave
estudantes = [
    {"Nome": "Gustavo", "Notas": (10, 10, 10, 15)},
    {"Nome": "Lucas", "Notas": (15, 50, 0, 10)},
    {"Nome": "Matheus", "Notas": (50, 40, 10, 8)}
]
# criando um dicionário para organizar as opçoes do menu.
operacao = {
    "media": media,
    "total": total,
    "maximo": maximo

}
    # loop for que percorre a nossa lista de estudante e puxa os valores nome e notas
for estudante in estudantes:
    nome = estudante [ "Nome" ]
    nota = estudante [ "Notas" ]

# criando uma entrada de dados para que o usuário possa escolher as funções desejadas.
    input_operacao = input("Digite entre 'media', 'total' e 'maximo': ")

# print com nome do estudante formatado com f'string 
    print(f'Estudante {nome}')
    controla_operacao = operacao[input_operacao]
    print(controla_operacao(nota))

    '''
   if operacao == "media":
        print(f'Estudante: {nome} Media:{media(nota)}')
        print("")
    elif operacao == "total":
        print(f"Estudante: {nome}, sua soma das notas é de: {total}")
    else:
        operacao == "maximo"
        print( f"Estudante {nome}, Nota maxima foi a de: {maximo(nota)}")
        '''