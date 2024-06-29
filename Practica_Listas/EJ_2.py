from random import randint
#! Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.

caracteres = []

for i in range(10):
    letra = chr(randint(65, 90)).lower()    #l Asignamos a letra caracteres segun tabla ASCII de forma aleatoria
    caracteres.insert(i, letra)             #l y aplicamos .lower() para pasar a minusculas.
print(caracteres)

vocales = ('a', 'e', 'i', 'o', 'u')

caracteres_sin_vocales = ""
for caracter in caracteres:
    if caracter not in vocales:
        caracteres_sin_vocales = caracteres_sin_vocales + caracter
print(list(caracteres_sin_vocales))
'''
l Se podria haber utilizado el metodo .replace, pero dada la naturalidad del array no permite su utilizacion,
l funciona solo con cadenas de strings, entonces se utilizo un ciclo for donde por cada caracter en la lista
l de caracteres se evaluo si dicho caracter no estaba presente en la lista de vocales. Si no se encontraban
l presente la vocal, el caracter se suma a la lista de caracteres sin vocales, continuo a esto se lista
l e imprime.
'''