lista = ['limón', 'manzana', 'naranja', 'plátano', 'cereza', 'fresa', 'tomate']

elemento_de_interes = 'cereza'

def buscar(elemento_de_interes, l):
    for index, element in enumerate(l):
        if element == elemento_de_interes:
            return index
    return -1

print(buscar(elemento_de_interes, lista))