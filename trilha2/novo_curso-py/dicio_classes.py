#dicionario contendo as infos do meu aluno 
meu_estudante = {
    "nome": "gustavo",
    "nota": [5,10,6]
}
# classe que recebe um argumento e no retorno soma a nota e divide pelo len.
def averiguar_nota(nota):
   return sum(nota["nota"])/ len(nota["nota"])

# esse print é nosso output chamando a classe e passando o dicio como param.
print(averiguar_nota(meu_estudante))

