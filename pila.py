class Stack:
    
    def __init__(self):
        self.__elements = [] #* El metodo __init__ (metodo constructor) instancia una clase, y inicializa el objeto q se crea.
                            #! El metodo self es el inicializador de la variable, similar al .this de java.
    
    def push(self, element): #Apila, agrega un elemento a la lista.
        self.elements.append(element)
        """
        #* El metodo push cumple la funcion de apilar, mediante el metodo .append. 
        #! Agregamos un metodo .append() por que tiene que entrar en el ultimo lugar de la lista, con el parametro element. 
        #? Y utilizaramos el metodo .insert() tendriamos q indicar la 
            #? posicion para insertar el elemento en una posicion particular de la lista.
        """
    
    def pop(self): #Desapila, quita el ultimo elemento de la pila.
        if len(self.elements) > 0: #todo Verifico que hallan elementos en la lista, comparando la cantidad de elementos > 0.
            return self.elements.pop() #* No se indica el parametro al metodo .pop(), ya que elimina el ultimo elemento de la lista por defecto (pila).
                                        #! Lo retornamos asi no perdemos el elemento eliminado.    
        else:
            return None #!Retorna None, asi evitamos que se rompa el .pop() al querer eliminar un dato que no se encuentre en la lista.    
    def on_top(self): #* Nos indica que elemento se encuentra en el top de la pila, no es necesario printear, unicamente retornar.
        if len(self.elements) > 0:
            return self.elements[-1] # Retorna el elemento en la posicion [-1], en otras palabras, la ultima posicion.
        else:
            return None

    def size(self):
        return len(self.elements) #! La funcion len() retorna el numero de valores que se encuentran en la lista.

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



#!Ejemplo del .append
"""
#p fruits = ['apple', 'banana', 'cherry']
#p fruits.append("orange")
#p print(fruits)
"""