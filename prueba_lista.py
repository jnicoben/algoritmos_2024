lista_de_elementos = [1, 20, 5, 67, 3, 4, -1]
print("Lista de elementos: ", lista_de_elementos)
print()

#! Insertar con posicion
lista_de_elementos.insert(2, 99) #l (Index, Values)
#! Insertar sin posicion
lista_de_elementos.append(123)  #l Inserta el elemento en la ultima posicion.
#! Eliminar un elemento de la lista (Suponiendo valores unicos)
#l El .remove elimina elementos por value.
#l El .pop elimina por posicion.
try:
    lista_de_elementos.remove(101) #l Indicamos el value. 
except ValueError:
    print('El elemento a eliminar no esta en la lista')
#l Si el elemento no existe rompe el codigo. Para evitar esto utilizamos un try.
#! Tamanio
print("Cantidad de elementos: ")
print(len(lista_de_elementos))
#! Ordenar de Menor a Mayor
lista_de_elementos.sort()   #l Metodo propio de la lista el .sort, es de los mas eficientes. Ordena cadenas segun la tabla ascii.
#! Ordenar de Mayor a Menor
lista_de_elementos.sort(reverse=True)
#! Busqueda
try:
    print('posicion', lista_de_elementos.index(21))
except ValueError:
    print('El elemento que busca no esta en la listas')
#! Barrido
print("Listado de elementos: ")
for element in lista_de_elementos:
    print(element)
#! Criterios de orden
#l Al comparar dos diccionarios, nos va a tirar error dado que al tener muchos atributos
#l la maquina no puede interpretar cual es menor o mayor. Para resolver esto es necesario
#l llamar a una funcion, para definir como quiero que se compare y asi poder ordenarlo.
def by_name(item):
    return item['apellido']+item['nombre'] #l concatenamos apellido y nombre para que se ordene de esa forma mediante la funcion creada.
#! Ordenar elementos simples
lista_de_elementos.sort(key=by_name) #l Ordenamos por nombre.