class Stack:
    def __init__(self):
        self.elements = [] #El self es el inicializador de la variable, similar al .this de java.
    def push(self, element): #El push seria el apilar, con append. 
        #Agregamos un metodo .append() por que tiene que entrar en el ultimo lugar de la lista. 
        #Y en el insert tendriamos q indicar la posicion.
        self.elements.append(element)
    def pop(self):
        pass
    def on_top(self):
        pass
    def size(self):
        pass

#Ejemplo del .append
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
