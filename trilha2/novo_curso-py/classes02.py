# este programa irá fazer consultas de três tipos de média. a soma, média e a nota maxima.

opcoes = {
    "media": lambda a : sum(a) / len(a),
    "soma": lambda b : sum(b),
    "total": lambda c: max(c)
}

estudantes = [
{"nome": "Gustavo","nota": (12, 15, 20)},
{"nome": "Madeus","nota": (12, 30, 8)},
{"nome": "Lucão","nota": (15, 0, 30)},
]

for estudante in estudantes:
    nome = estudante["nome"]
    notas = estudante["nota"]

    print(f"Estudante {nome}")
    in_user = input("Digite entre media, soma e total: ")
    ctl_input = opcoes[in_user]
    print (ctl_input(notas))