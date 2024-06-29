'''
Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad
de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además
la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
a. obtener la cantidad de Pokémons de un determinado entrenador;
b. listar los entrenadores que hayan ganado más de tres torneos;
c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
d. mostrar todos los datos de un entrenador y sus Pokémos;
e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
(tipo y subtipo);
g. el promedio de nivel de los Pokémons de un determinado entrenador;
h. determinar cuántos entrenadores tienen a un determinado Pokémon;
i. mostrar los entrenadores que tienen Pokémons repetidos;
j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion
o Wingull;
k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
deberán mostrar los datos de ambos;
'''

from random import choice
from lista import show_list_list, by_name, search

entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60
    }
]

pokemons = [
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Pikachu",
        "nivel": 20,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },
    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "nombre": "Tyrantrum",
        "nivel": 41,
        "tipo": "Roca",
        "subtipo": "Dragon"
    },
    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "nombre": "Terrakion",
        "nivel": 41,
        "tipo": "Roca",
        "subtipo": "Lucha"
    },
    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Wingull",
        "nivel": 27,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": None
    },
    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },
    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Dragonite",
        "nivel": 55,
        "tipo": "Dragón",
        "subtipo": "Volador"
    },
    {
        "nombre": "Aerodactyl",
        "nivel": 52,
        "tipo": "Roca",
        "subtipo": "Volador"
    }
]

names = ["Ash Ketchum", "Goh", "Leon", "Chloe", "Raihan"]

lista_entrenadores = []

for entrenador in entrenadores:
    entrenador.update({'sublist': []})
    lista_entrenadores.append(entrenador)

for pokemon_name in pokemons:
    pos = search(lista_entrenadores, 'nombre', choice(names))
    if pos is not None:
        lista_entrenadores[pos]['sublist'].append(pokemon_name)
    else:
        print('no existe el entrenador')

lista_entrenadores.sort(key=by_name)
show_list_list('Entrenadores', 'Pokemons', lista_entrenadores)


#l obtener la cantidad de Pokémons de un determinado entrenador;
print('Entrenadores: Ash Ketchum, Goh, Leon, Chloe, Raihan')
nombre_entrenador = input("ingrese el nombre del entrenador \n")
index_list_entren = search(lista_entrenadores,'nombre', nombre_entrenador)
print(f'El entrenador {nombre_entrenador}, tiene un total de ', len(lista_entrenadores[index_list_entren]['sublist']), 'pokemons.')
print(lista_entrenadores[index_list_entren]['sublist'])

#l listar los entrenadores que hayan ganado más de tres torneos;
campeones = []
for index_entrenador, entrenador in enumerate(lista_entrenadores):
    if lista_entrenadores[index_entrenador]['torneos_ganados'] > 3:
        campeones.append(lista_entrenadores[index_entrenador]['nombre'])
print('Lo entrenadores que tienen mas de 3 torneos ganados son: ', campeones)

#l el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
print()
mayor = float('-inf')
for index_entrenador, entrenador in enumerate(lista_entrenadores):
    entrenador2 = lista_entrenadores[index_entrenador]['torneos_ganados']
    if lista_entrenadores[index_entrenador]['torneos_ganados'] > lista_entrenadores[index_entrenador - 1]['torneos_ganados'] and lista_entrenadores[index_entrenador]['torneos_ganados'] > mayor:
        mayor = lista_entrenadores[index_entrenador]['torneos_ganados']
        name_champ = lista_entrenadores[index_entrenador]['nombre']
index_pokemon_champ = search(lista_entrenadores, 'nombre', name_champ)
print("El entrenador con mas torneos ganados es ", lista_entrenadores[index_pokemon_champ]['nombre'],
       'con un total de ', lista_entrenadores[index_pokemon_champ]['torneos_ganados'], 'torneos ganados.')

most_lvl = 0
for pokemon_name in lista_entrenadores[index_pokemon_champ]['sublist']:
    pokemon_lvl = pokemon_name['nivel']
    if pokemon_lvl > most_lvl:
        most_lvl = pokemon_lvl

index_most_lvl = search(lista_entrenadores[index_pokemon_champ]['sublist'],'nivel',most_lvl)
name_most_lvl = lista_entrenadores[index_pokemon_champ]['sublist'][index_most_lvl]['nombre']
lvl_most_lvl = lista_entrenadores[index_pokemon_champ]['sublist'][index_most_lvl]['nivel']
print("El pokemon con mas nivel es ", name_most_lvl,'con un nivel de ', lvl_most_lvl)

#l d. mostrar todos los datos de un entrenador y sus Pokémos;
print()
name_entrenador = input("Inserte el nombre del entrenador de cual desea conocer sus datos y pokemons: \n")
index_name_entrenador = search(lista_entrenadores, 'nombre', name_entrenador)
print(lista_entrenadores[index_name_entrenador])

#l e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
print()
print('Los entrenadores cuyo porcentaje de batallas ganadas es mayor al 79% son:')
for index_battle, trainer in enumerate(entrenadores):
    battles_won = entrenadores[index_battle]['batallas_ganadas']
    lost_battles = entrenadores[index_battle]['batallas_perdidas']
    trainer_name = entrenadores[index_battle]['nombre']
    
    total_battles = battles_won + lost_battles
    win_rate = (battles_won / total_battles) * 100
    if win_rate > 79:
        win_win = win_rate
        print('-', trainer_name, win_win)

#l f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
print()
print("Entrenadores que tengan Pokemons tipo Fuego, Planta y Agua/Volador: ")
list_type = []
for trainer in lista_entrenadores:
    for i_pokemon_type, pokemon_type in enumerate(trainer['sublist']):
        if (pokemon_type['tipo'] == 'Agua' and  pokemon_type['subtipo'] == 'Volador') or pokemon_type['tipo'] == 'Fuego' or  pokemon_type['tipo'] == 'Planta':
            print('-', trainer['nombre'],
                   pokemon_type['nombre'], pokemon_type['tipo'], pokemon_type['subtipo'])

#l g. el promedio de nivel de los Pokémons de un determinado entrenador;
print()
sum_total = 0
trainer_select = input("Ingrese el nombre del entrenador del que desea conocer el promedio de los Pokemons: ")
index_trainer_select = search(lista_entrenadores, 'nombre', trainer_select)
for trainer in lista_entrenadores[index_trainer_select]['sublist']:
        sum_total += trainer['nivel']
if len(lista_entrenadores[index_trainer_select]['sublist']) > 0:
    prom_total = sum_total / len(lista_entrenadores[index_trainer_select]['sublist'])
else:
    print("El entrenador no tiene Pokemons")
print("El promedio de nivel de los pokemones del entrenador ",trainer_select, " es de ", prom_total)

#l h. determinar cuántos entrenadores tienen a un determinado Pokémon;
print()
pokemon_selected = input("Ingrese el nombre del Pokemon: ")
trainer_pokemons_repeated = []

for trainer_pokemon in lista_entrenadores:
    for pokemon_name in trainer_pokemon['sublist']:
        if pokemon_selected == pokemon_name['nombre']:
            trainer_pokemons_repeated.append(trainer_pokemon['nombre'])
print(f"El numero de entrenadores que tienen a {pokemon_selected} es de {len(trainer_pokemons_repeated)}, y son: ")
print(trainer_pokemons_repeated)

#l i. mostrar los entrenadores que tienen Pokémons repetidos;
print()
pokemons_name = []
unique_pokemons = []

for trainer in lista_entrenadores:
    for pokemons in trainer['sublist']:
        pokemons_name.append(pokemons['nombre'])#l Cargo los nombres de los entrenadores a una nueva lista.
    if len(pokemons_name) != len(set(pokemons_name)): #l Comparo la lista de nombres de pokemons con la lista de datos unicos.
        unique_pokemons = set(pokemons_name)
        unique_pokemons_list = list(unique_pokemons) #l Transformo el set a lista mediante list() | {1, 2, 3} --> [1, 2, 3]
        print(trainer['nombre']+": ", end="")
        for i in range (len(unique_pokemons_list)):
            pokemons_name.remove(unique_pokemons_list[i])
        for pokemon_name in pokemons_name:
            print(pokemon_name+" | ",end="")
        print("")
    else:
        print(f"El entrenador {trainer['nombre']} no tiene Pokemons repetidos.")
    pokemons_name.clear() #l Mediante clear(), vaciamos la lista, para que en la proxima vuelta no tenga nada.
    unique_pokemons.clear() 
print("")

#l j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
list_pokemons_repeat = []
for trainer in lista_entrenadores:
    print(trainer['nombre'])  
    for pokemon in trainer['sublist']:
        if pokemon['nombre'] == 'Tyrantrum' or pokemon['nombre'] == 'Terrakion' or pokemon['nombre'] == 'Wingull':
            list_pokemons_repeat.append(pokemon['nombre'])
    if len(list_pokemons_repeat) > 0:
        print(list_pokemons_repeat)
    else:
        print("No tiene ninguno de los siguientes Pokemons: Tyrantrum, Terrakion, Wingull.")
    list_pokemons_repeat.clear()

#l k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
#l como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
#l deberán mostrar los datos de ambos;

trainer_x = input("Ingrese el nombre del entrenador \n")
pokemon_y = input("Ingrese el nombre del Pokemon \n")

for trainer in lista_entrenadores:
    if trainer['nombre'] == trainer_x:
        for pokemon in trainer['sublist']:
            if pokemon['nombre'] == pokemon_y:
                print(f"El entrenador {trainer_x} tiene al Pokemon {pokemon_y}")
                print(trainer)