#Inserindo 10 valores não repetir em lista

from random import randint

lista = []

def insere():
    cont = 0
    while cont < 10:
        n = randint(0,100)
        if n not in lista:
            lista.append(n)
            cont = cont + 1
        listaordenada = sorted(lista)
    return listaordenada

print(insere())