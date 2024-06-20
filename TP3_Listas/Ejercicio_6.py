'''
Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,

casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
rias para poder realizar las siguientes actividades:

a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
“traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
sea anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que comienzan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic.
'''

from lista import search, by_name, by_house, remove, show_list, by_year
def by_year(item):
    return item['año_aparicion']


super_heroes = [
  {
    "nombre": "Linterna Verde",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
  },
  {
    "nombre": "Wolverine",
    "año_aparicion": 1974,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
  },
  {
    "nombre": "Doctor Strange",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
  },
  {
    "nombre": "Capitana Marvel",
    "año_aparicion": 1968,
    "casa_comic": "Marvel Comics",
    "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
  },
  {
    "nombre": "Mujer Maravilla",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
  },
  {
    "nombre": "Flash",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
  },
  {
    "nombre": "Star-Lord",
    "año_aparicion": 1976,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
  },
  {
    "nombre": "Superman",
    "año_aparicion": 1938,
    "casa_comic": "DC Comics",
    "biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
  },
  {
    "nombre": "Batman",
    "año_aparicion": 1939,
    "casa_comic": "DC Comics",
    "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
  },
  {
    "nombre": "Iron Man",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
  },
  {
    "nombre": "Wonder Woman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
  },
  {
    "nombre": "Spider-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."
  },
  {
    "nombre": "Thor",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
  },
  {
    "nombre": "Aquaman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
  },
  {
    "nombre": "Green Arrow",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
  },
  {
    "nombre": "Hulk",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
  },
  {
    "nombre": "Black Widow",
    "año_aparicion": 1964,
    "casa_comic": "Marvel Comics",
    "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
  },
  {
    "nombre": "Mr. Fantástico",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
  },
  {
    "nombre": "La Mujer Invisible",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
  },
  {
    "nombre": "La Antorcha Humana",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
  },
  {
    "nombre": "La Cosa",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
  },
  {
    "nombre": "Capitán América",
    "año_aparicion": 1941,
    "casa_comic": "Marvel Comics",
    "biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
  },
  {
    "nombre": "Ant-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Hanbiografiak Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos. Usa un traje que lo hace pequeño."
  }
]
'''
a. eliminar el nodo que contiene la información de Linterna Verde;
'''
print()
index_linterna_verde = search(super_heroes, 'nombre', 'Linterna Verde')
super_heroes2 = super_heroes
super_heroes2.pop(index_linterna_verde)
print(super_heroes2)

'''
b. mostrar el año de aparición de Wolverine;
'''
print()
index = search(super_heroes, 'nombre', 'Wolverine') #l Asignamos a la variable index la posicion del criterio nombre con valor Wolverine.
print('El super heroe ', super_heroes[index]['nombre'], f' se ubica en la posicion {index} de la lista de Super Heroes.')
if index is not None:
    superHeroe = super_heroes[index]
    print('El año de aparicion de', superHeroe['nombre'], 'fue', superHeroe['año_aparicion'])
'''
c. cambiar la casa de Dr. Strange a Marvel;
'''
print()
index_drs = search(super_heroes, 'nombre', 'Doctor Strange')
if index_drs is not None:
    super_heroes[index_drs]['casa_comic'] = 'Marvel'
    print('- El super heroe ', super_heroes[index_drs]['nombre'], 'ahora pertenece a la casa', super_heroes[index_drs]['casa_comic'])
'''
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
“traje” o “armadura”;
'''
print()
for index_t_a in range(len(super_heroes)):
    if 'traje' in super_heroes[index_t_a]['biografia'] or 'armadura' in super_heroes[index_t_a]['biografia']:
        print('-', index_t_a, super_heroes[index_t_a]['nombre'], super_heroes[index_t_a]['biografia'])
'''
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
sea anterior a 1963;
'''
print()
for index_1963 in range(len(super_heroes)):
  super_heroes.sort(key=by_year)
  if (super_heroes[index_1963]['año_aparicion'] < 1963):
      print(super_heroes[index_1963]['año_aparicion'], super_heroes[index_1963]['nombre'], super_heroes[index_1963]['casa_comic'])

'''
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
'''
print()
index_capitana_marvel = search(super_heroes, 'nombre', 'Capitana Marvel')
index_mujer_maravilla = search(super_heroes, 'nombre', 'Mujer Maravilla')

print('Capitana Marvel pertenece a la casa de ', super_heroes[index_capitana_marvel]['casa_comic'],
       ', mientras que la Mujer Maravilla pertenece a la casa de ',
         super_heroes[index_mujer_maravilla]['casa_comic'])

'''
g. mostrar toda la información de Flash y Star-Lord;
'''
print()
index_flash = search(super_heroes, 'nombre', 'Flash')
index_star_lord = search(super_heroes, 'nombre', 'Star-Lord')
print(super_heroes[index_flash], '\n', super_heroes[index_star_lord])
'''
h. listar los superhéroes que comienzan con la letra B, M y S;
'''
print()
super_heroes.sort(key=by_name)
for index, heroe in enumerate(super_heroes):
    if heroe['nombre'].startswith(('B', 'S', 'M')):
        print(heroe['nombre'])
'''
i. determinar cuántos superhéroes hay de cada casa de comic.
'''
print()
count = 0
count2 = 0
for index, heroe in enumerate(super_heroes):
    if super_heroes[index]['casa_comic'] == 'Marvel Comics':
        count = count + 1
    else:
        count2 = count2 + 1
print(f'En Marvel Comics hay {count} super heroes')
print(f'En DC Comics hay {count2} super heroes')