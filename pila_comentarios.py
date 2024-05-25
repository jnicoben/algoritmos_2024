
class Stackk:
    
    def __init__(self):
        self.__elements = [] 
            #* El metodo __init__ (metodo constructor) instancia una clase, y inicializa el objeto q se crea.
            #! El metodo self es el inicializador de la variable, similar al .this de java.
            #l Le agregamos un __ a elements para transformar el atributo en un atributo privado __elements.
            #l Con esto restringimos a que el usuario (desarrollador) interactue unicamente con los metodos expresados en la clase. 
    
    def push(self, element): #Apila, agrega un elemento a la lista.
        self.__elements.append(element)
            #* El metodo push cumple la funcion de apilar, mediante el metodo .append. 
            #! Agregamos un metodo .append() por que tiene que entrar en el ultimo lugar de la lista, con el parametro element. 
            #? Y utilizaramos el metodo .insert() tendriamos q indicar la 
            #? posicion para insertar el elemento en una posicion particular de la lista.
    
    def pop(self): #Desapila, quita el ultimo elemento de la pila.
        if len(self.__elements) > 0: #todo Verifico que hallan elementos en la lista, comparando la cantidad de elementos > 0.
            return self.__elements.pop() #* No se indica el parametro al metodo .pop(), ya que elimina el ultimo elemento de la lista por defecto (pila).
                                        #! Lo retornamos asi no perdemos el elemento eliminado.    
        else:
            return None #!Retorna None, asi evitamos que se rompa el .pop() al querer eliminar un dato que no se encuentre en la lista.    
    def on_top(self): #* Nos indica que elemento se encuentra en el top de la pila, no es necesario printear, unicamente retornar.
        if len(self.__elements) > 0:
            return self.__elements[-1] # Retorna el elemento en la posicion [-1], en otras palabras, la ultima posicion.
        else:
            return None

    def size(self):
        return len(self.__elements) #! La funcion len() retorna el numero de valores que se encuentran en la lista.


"""
pila = Stack() #todo Instanciamos un objeto.
pila.push(12)
pila.push(1)
pila.push(20)


print(pila.elements)
print(pila.on_top())
print(pila.size())
print()
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
print(pila.pop())
"""
#! Como no podemos acceder a todos los elementos de la pila por cambiar la privacidad del __elements, tenemos q encontrar la forma de hacerlo.
#todo Esta es la forma para hacer un barrido a una pila de forma correcta, mientras que sea necesario que el elemento no se pierda, para esto la lista auxiliar.

from random import randint #todo randint, funcion que devuelve un numero randomico.

pila = Stackk()
pila_aux = Stackk() #!En ella almacenamos los valores de pila original, asi cuando hacemos el barrido (listamos, y aplicamos el pila.pop) no se pierden los valores.

for i in range(10):
    pila.push(randint(1, 99))

print(pila.on_top())
print(pila.size())
print()

#! Listar
while pila.size() > 0:
    data = pila.pop()
    print(data)
    pila_aux.push(data)

print()
#! Reconstruccion
while pila_aux.size() > 0:
    pila.push(pila_aux.pop())

print()
print(pila.size())
print(pila.on_top())

#!Forma de hacer un barrido en una pila, mediante una pila auxiliar, donde tengo que sacar todo, pasarlo a una pila auxiliar y reconstruir la pila.
#!Pila A y Pila B
"""
    4       1
    3       2
    2       3
    1       4
"""
#l podemos resolver todos, del 1 al 24.


#!Ejemplo del .append
"""
#p fruits = ['apple', 'banana', 'cherry']
#p fruits.append("orange")
#p print(fruits)
"""

#!CUANDO UTILIZAMOS UNA LIBRERIA, NO TENEMOS QUE DEJAR CODIGO EJECUTABLE. POR ESO LA CREACION DE ESTA CLASE.
#* Al NOMBRE DE LA CLASE LO MODIFIQUE POR STACKK, ASI NO LLAMA A ESTA CLASE LA PILA.