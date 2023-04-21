media = lambda seq: len(seq) / sum (seq)
total = lambda seq: sum(seq)
maximo = lambda seq: max(seq)

estudantes = [
    {"Nome": "Gustavo", "Notas": (10, 10, 10, 15)},
    {"Nome": "Lucas", "Notas": (15, 50, 0, 10)},
    {"Nome": "Matheus", "Notas": (50, 40, 10, 8)}
]

for estudante in estudantes:
    nome = estudante [ "Nome" ]
    nota = estudante [ "Notas" ]

    operacao = input("Digite entre 'media', 'total' e 'maximo': ")

    if operacao == "media":
        print(f'Estudante: {nome}; Media:{media(nota)}')
        print("")
