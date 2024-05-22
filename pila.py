class Stack:
    def __init__(self):
        self.elements = [] #*El self es el inicializador de la variable, similar al .this de java.
    def push(self, element): 
        self.elements.append(element)
        #! El push seria el apilar, con append. 
        #! Agregamos un metodo .append() por que tiene que entrar en el ultimo lugar de la lista. 
        # Y el metodo .insert() tendriamos q indicar la 
        # posicion para insertar el elemento en una posicion particular de la lista.
    
    def pop(self):
        self.elements.pop() #*No se indica el parametro al metodo .pop(), ya que elimina el ultimo elemento de la lista por defecto (pila).
    def on_top(self):
        pass
    
    def size(self):
        pass

#!Ejemplo del .append
"""
fruits = ['apple', 'banana', 'cherry']
!fruits.append("orange")
print(fruits)
"""