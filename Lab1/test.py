import requests

# Obtener todas las películas
response = requests.get('http://localhost:5000/peliculas')
peliculas = response.json()
print("Películas existentes:")
for pelicula in peliculas:
    print(f"ID: {pelicula['id']}, Título: {pelicula['titulo']}, Género: {pelicula['genero']}")
print()

# Agregar una nueva película
nueva_pelicula = {
    'titulo': 'Pelicula de prueba',
    'genero': 'Acción'
}
response = requests.post('http://localhost:5000/peliculas', json=nueva_pelicula)
if response.status_code == 201:
    pelicula_agregada = response.json()
    print("Película agregada:")
    print(f"ID: {pelicula_agregada['id']}, Título: {pelicula_agregada['titulo']}, Género: {pelicula_agregada['genero']}")
else:
    print("Error al agregar la película.")
print()

# Obtener detalles de una película específica
id_pelicula = 1  # ID de la película a obtener
response = requests.get(f'http://localhost:5000/peliculas/{id_pelicula}')
if response.status_code == 200:
    pelicula = response.json()
    print("Detalles de la película:")
    print(f"ID: {pelicula['id']}, Título: {pelicula['titulo']}, Género: {pelicula['genero']}")
else:
    print("Error al obtener los detalles de la película.")
print()

# Actualizar los detalles de una película
id_pelicula = 1  # ID de la película a actualizar
datos_actualizados = {
    'titulo': 'Nuevo título',
    'genero': 'Comedia'
}
response = requests.put(f'http://localhost:5000/peliculas/{id_pelicula}', json=datos_actualizados)
if response.status_code == 200:
    pelicula_actualizada = response.json()
    print("Película actualizada:")
    print(f"ID: {pelicula_actualizada['id']}, Título: {pelicula_actualizada['titulo']}, Género: {pelicula_actualizada['genero']}")
else:
    print("Error al actualizar la película.")
print()

# Eliminar una película
id_pelicula = 1  # ID de la película a eliminar
response = requests.delete(f'http://localhost:5000/peliculas/{id_pelicula}')
if response.status_code == 200:
    print(f"Película ID: {id_pelicula} eliminada correctamente.")
else:
    print("Error al eliminar la película.")
print()

# Obtener peliculas por un genero
genero = 'Ciencia ficción'
response = requests.get(f'http://localhost:5000/peliculas/genero/{genero}')
if response.status_code == 200:
    peliculas = response.json()
    print("Películas por género:")
    for pelicula in peliculas:
        print(f"ID: {pelicula['id']}, Título: {pelicula['titulo']}, Género: {pelicula['genero']}")
else:
    print("Error al obtener las películas por género.")
print()

# Buscar peliculas por un titulo
titulo = 'In'
response = requests.get(f'http://localhost:5000/peliculas/buscar/{titulo}')
if response.status_code == 200:
    peliculas = response.json()
    print("Películas por título:")
    for pelicula in peliculas:
        print(f"ID: {pelicula['id']}, Título: {pelicula['titulo']}, Género: {pelicula['genero']}")
else:
    print("Error al buscar las películas por título.")
print()

# Obtener una pelicula random sugerida
response = requests.get('http://localhost:5000/peliculas/sugerir')
if response.status_code == 200:
    pelicula_sugerida = response.json()
    print("Película sugerida:")
    print(f"ID: {pelicula_sugerida['id']}, Título: {pelicula_sugerida['titulo']}, Género: {pelicula_sugerida['genero']}")
else:
    print("Error al obtener la película sugerida.")
print()

# Obtener una pelicula random sugerida por genero
genero = 'Acción'
response = requests.get(f'http://localhost:5000/peliculas/sugerir/{genero}')
if response.status_code == 200:
    pelicula_sugerida = response.json()
    print(f"Película sugerida de género {genero}:")
    print(f"ID: {pelicula_sugerida['id']}, Título: {pelicula_sugerida['titulo']}, Género: {pelicula_sugerida['genero']}")
else:
    print("Error al obtener la película sugerida por género.")
print()
