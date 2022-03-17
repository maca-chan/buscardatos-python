lista = ['cereza', 'fresa', 'limón', 'manzana', 'naranja', 'plátano', 'tomate'] 
posicion = int(len(lista)/2)
elemento_de_interes = 'cereza'

def buscar(lista, posicion, elemento_de_interes):
    if lista[posicion] == elemento_de_interes:
        return posicion
    elif lista[posicion] > elemento_de_interes:
        return buscar(lista, int(posicion/2), elemento_de_interes)
    else:
        return buscar(lista, posicion+int(posicion/2), elemento_de_interes)

print(buscar(lista, posicion, elemento_de_interes))