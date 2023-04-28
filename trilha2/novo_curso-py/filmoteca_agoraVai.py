menu_usr = "aperte a para adcionar um filme, l para ver filme, f para achar o filme e q para sair: "

# lista de filems.
filmes = []


#função que adciona os filmes e coloca na lista (filmes) que foi instaciada acima.
def add_filme():
    titulo = input("Digite o título do filme: ")
    diretor = input("Digite o nome do diretor: ")
    ano = input("Digite o ano do filme: ")
# dando um apend em uma lista, o elemento é um dicio.
    filmes.append(
        {"titulo": titulo,
         "diretor": diretor,
         "ano": ano
    })


def mostrar_filme():
    for mostrar in mostrar_filme:
        printar_filme(mostrar)


def printar_filme():
    print(f"titulo: {mostrar_filme['titulo']}")
    print(f"diretor: {mostrar_filme['diretor']}")
    print(f"ano: {mostrar_filme['ano']}")


def encontrar_filme():
    input_pesquiar = input("Me diga o filme que você está procurando: ")

    for mostrar in mostrar_filme:
        if mostrar ['titulo'] == input_pesquiar:
            printar_filme(mostrar)


opcoes_usr = {
    "a": add_filme,
    "l": printar_filme,
    "f": encontrar_filme
}


def menu():
    selecao = input(menu_usr)
    while selecao != 'q':
        if selecao in opcoes_usr:
            funcao_selecionada = opcoes_usr[selecao]
            funcao_selecionada()
        else:
            print("Você digitou algo difretente.... tente outra vez! ")
             
        selecao = input(menu_usr)

    menu()


