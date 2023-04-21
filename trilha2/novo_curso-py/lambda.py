# def calcular_media (media): 
#    return sum(media) / len(media)

calcular_media = lambda media:sum(media)/len(media)


lista_medias = [
    {"Nome" : "Gustavo", "Nota": (10, 15, 30, 10)},
    {"Nome" : "Lucas", "Nota": (15, 20, 30, 40)},
    {"Nome" : "Matheus", "Nota": (15, 30 , 45)},
]



for medias in lista_medias:
    print( calcular_media( medias['Nota'] ) )