

class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, element):  #l Llega un elemento, puede arribar una persona, objeto, etc. Siempre por el final de la cola.
        self.__elements.append(element)
    def attention(self): #l Comprobamos si hay mas de cero elementos.
        if len(self.__elements) > 0:
            return self.__elements.pop(0) #l le indicamos al .pop que quite el elemento ubicado en el inicio de la cola.
        else:
            return None
        
    def size(self):
        return len(self.__elements) #l Pedimos que retorne el tamaño del elemento.
    
    def on_front(self):
        if len(self.__elements) > 0:
            return self.__elements[0] #l Retorna el elemento ubicado en la posicion [0].
        else:
            return None
        
    def move_to_end(self):
        element = self.attention()
        if element is not None:
            self.arrive(element) #l Mueve el elemento del principio de la cola al final.
    


#! Mostrar todos los elementos
    
cola_1 = Queue()
cola_1.arrive(1)
cola_1.arrive(2)
cola_1.arrive(3)
cola_1.arrive(4)
cola_1.arrive(5)
print(cola_1.size())
print(cola_1.on_front())
for i in range(cola_1.size()):
    print(cola_1.on_front())
    cola_1.move_to_end()
print()
print(cola_1.size())