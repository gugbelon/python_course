#                               FUNCAO RISE

#serve para a gente já dizer o erro caso ele aconteça. 

# se o n for maior que três ele vai entrar no rise e vai ter meu print mais bonito.


def frutas (n):
    lista = ['banana','cereja','melao',"amora", 'pessego']
    if n >3:
        raise IndexError("O valor excede o número de elementos da lista")
    else:
        return lista[n]
    
print(frutas(5))
