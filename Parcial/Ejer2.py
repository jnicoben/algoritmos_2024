from pila import Stack
pila = Stack ()
pila2 = Stack ()
pila_aparte = Stack ()

diccionario = {'Tyranosaurio':'6','Wolverine':'7',"Hulk":'3', 'Viuda negra':'2', 'Rocket Raccoon':'1','Doctor Strange':'4','Groot':'2', 'Capitan america':'7', 'Thor':'5', 'Iron man':'8', 'Pantera negra':'3', 'Ciclope':'6','Magneto':'6','Deadpool':'5', 'Gamora':'2'}

dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": 7000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": 6000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": 15,
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": 56000,
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": 5000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": 10000,
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": 2000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": 23000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": 15000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": 6000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": 2500,
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": 1500,
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": 2700,
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": 5000,
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": 25,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": 200,
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": 450,
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": 15000,
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]

#! Contar cuantas especies hay.
for i in range(len(dinosaurios)): 
  dato = dinosaurios[i] 
  pila.push(dato)
  dato = pila.pop()
  pila2.push(dato)
  if dato['especie'] == 'Theropoda':
    theropoda = 1
  if dato['especie'] == 'Ceratopsidae':
    ceratopsidae = 1
  if dato['especie'] == 'Sauropoda':
    sauropoda = 1
  if dato['especie'] == 'Pterosauria':
    pterosauria = 1
  if dato['especie'] == 'Dromaeosauridae':
    dromaeosauridae = 1
  if dato['especie'] == 'Stegosauridae':
    stegosauridae = 1
  if dato['especie'] == 'Ankylosauridae':
    ankylosauridae = 1
  if dato['especie'] == 'Hadrosauridae':
    hadrosauridae = 1
  if dato['especie'] == 'Therizinosauridae':
    therizinosauridae = 1
  if dato['especie'] == 'Spinosauridae':
    spinosauridae = 1
  if dato['especie'] == 'Plesiosauria':
    plesiosauria = 1
  if dato['especie'] == 'Mosasauridae':
    mosasauridae = 1

cantidad_especies = theropoda+ceratopsidae+sauropoda+pterosauria+dromaeosauridae+stegosauridae+ankylosauridae+hadrosauridae+therizinosauridae+spinosauridae+plesiosauria+mosasauridae
print("La cantidad de especies es:",cantidad_especies)

#! Determinar cuantos descubridores distintos hay.
for i in range(len(dinosaurios)): 
  dato = pila2.pop()
  pila.push(dato)
  if dato['descubridor'] == 'Barnum Brown':
    descubridor1 = 1
  if dato['descubridor'] == 'Othniel Charles Marsh':
    descubridor2 = 1
  if dato['descubridor'] == 'Henry Fairfield Osborn':
    descubridor3 = 1
  if dato['descubridor'] == 'Elmer S. Riggs':
    descubridor4 = 1
  if dato['descubridor'] == 'William Conybeare':
    descubridor5 = 1
  if dato['descubridor'] == 'Ernst Stromer':
    descubridor6 = 1
  if dato['descubridor'] == 'William Parks':
    descubridor7 = 1
  if dato['descubridor'] == 'José Bonaparte':
    descubridor8 = 1
  if dato['descubridor'] == 'Lawrence Lambe':
    descubridor9 = 1
  if dato['descubridor'] == 'Evgeny Maleev':
    descubridor10 = 1
  if dato['descubridor'] == 'Douglas A. Lawson':
    descubridor11 = 1
  if dato['descubridor'] == 'Mary Anning':
    descubridor12 = 1

cantidad_desc = descubridor1+descubridor2+descubridor3+descubridor4+descubridor5+descubridor6+descubridor7+descubridor8+descubridor9+descubridor10+descubridor11+descubridor12
print("La cantidad de distintos descubridores es:",cantidad_desc)

#! Mostrar todos los dinosaurios que empiecen con T.
name_t = []
for i in range(len(dinosaurios)): 
  dato = pila.pop()
  pila2.push(dato)
  if 'T' in dato['nombre']:
    name_t.append(dato['nombre'])
print("Dinosaurios que su nombre empieza con T:")
for nombres in name_t:
  print(nombres,end=" ")

#! Mostrar todos los dinosaurio que pesen menos de 275 Kg.
print("")
dato_peso = []
for i in range(len(dinosaurios)):
  dato = pila2.pop()
  pila.push(dato)
  if dato['peso']<275:
    dato_peso.append(dato['nombre'])
print("Los dinosaurios que pesan menos de 275 kg:")
for nombres in dato_peso:
  print(nombres,end=" ")
print("")

#! Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S.
datos_aqs = []
for i in range(len(dinosaurios)):
  dato = pila.pop()
  if 'A' in dato['nombre']:
    datos_aqs.append(dato['nombre'])
    pila_aparte.push(dato['nombre'])
  if 'Q' in dato['nombre']:
    datos_aqs.append(dato['nombre'])
    pila_aparte.push(dato['nombre'])
  if 'S' in dato['nombre']:
    datos_aqs.append(dato['nombre'])
    pila_aparte.push(dato['nombre'])
print("Dinosaurios que comienzan con A, Q, S:")
for nombres in datos_aqs:
  print(nombres,end=" ")
print("")

"""
print("Dinosaurios que comienzan con A, Q, S:")
for i in range(pila_aparte.size()):
  print(pila_aparte.pop()+" ",end="")
"""




