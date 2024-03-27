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

from test_get import get_test
from test_post import post_test
from test_delete import delete_test

get_test()
post_test()
delete_test()