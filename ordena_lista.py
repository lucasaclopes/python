#Função que retorna lista ordenada

def ordenaLista():
    n = int(input("Quantos números sua lista terá? "))
    cont = 0
    lista = []
    while(cont < n):
        i = int(input("Número: "))
        lista.append(i)
        cont = cont + 1
    return sorted(lista)

print(ordenaLista())