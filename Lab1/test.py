# import requests

# # Agregar una nueva película
# nueva_pelicula = {
#     'titulo': 'Pelicula de prueba',
#     'genero': 'Acción'
# }
# response = requests.post('http://localhost:5000/peliculas', json=nueva_pelicula)
# if response.status_code == 201:
#     pelicula_agregada = response.json()
#     print("Película agregada:")
#     print(f"ID: {pelicula_agregada['id']}, Título: {pelicula_agregada['titulo']}, Género: {pelicula_agregada['genero']}")
# else:
#     print("Error al agregar la película.")
# print()


# # Actualizar los detalles de una película
# id_pelicula = 1  # ID de la película a actualizar
# datos_actualizados = {
#     'titulo': 'Nuevo título',
#     'genero': 'Comedia'
# }
# response = requests.put(f'http://localhost:5000/peliculas/{id_pelicula}', json=datos_actualizados)
# if response.status_code == 200:
#     pelicula_actualizada = response.json()
#     print("Película actualizada:")
#     print(f"ID: {pelicula_actualizada['id']}, Título: {pelicula_actualizada['titulo']}, Género: {pelicula_actualizada['genero']}")
# else:
#     print("Error al actualizar la película.")
# print()

# # Eliminar una película
# id_pelicula = 1  # ID de la película a eliminar
# response = requests.delete(f'http://localhost:5000/peliculas/{id_pelicula}')
# if response.status_code == 200:
#     print(f"Película ID: {id_pelicula} eliminada correctamente.")
# else:
#     print("Error al eliminar la película.")
# print()

from test_get import *
get_test()