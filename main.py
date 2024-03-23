import random
from flask import Flask, jsonify, request
from proximo_feriado import NextHoliday

app = Flask(__name__)
peliculas = [
    {'id': 1, 'titulo': 'Indiana Jones', 'genero': 'Acción'},
    {'id': 2, 'titulo': 'Star Wars', 'genero': 'Acción'},
    {'id': 3, 'titulo': 'Interstellar', 'genero': 'Ciencia ficción'},
    {'id': 4, 'titulo': 'Jurassic Park', 'genero': 'Aventura'},
    {'id': 5, 'titulo': 'The Avengers', 'genero': 'Acción'},
    {'id': 6, 'titulo': 'Back to the Future', 'genero': 'Ciencia ficción'},
    {'id': 7, 'titulo': 'The Lord of the Rings', 'genero': 'Fantasía'},
    {'id': 8, 'titulo': 'The Dark Knight', 'genero': 'Acción'},
    {'id': 9, 'titulo': 'Inception', 'genero': 'Ciencia ficción'},
    {'id': 10, 'titulo': 'The Shawshank Redemption', 'genero': 'Drama'},
    {'id': 11, 'titulo': 'Pulp Fiction', 'genero': 'Crimen'},
    {'id': 12, 'titulo': 'Fight Club', 'genero': 'Drama'}
]


def obtener_peliculas():
    return jsonify(peliculas)

def obtener_pelicula(id):
    # Lógica para buscar la película por su ID y devolver sus detalles
    # Considerando que todas las peliculas estan en orden con respecto a su ID 
    p_titulo = peliculas[id-1].get("titulo")
    p_gen = peliculas[id-1].get("genero")
    pelicula_encontrada = (p_titulo, p_gen)
    return jsonify(pelicula_encontrada)


def agregar_pelicula():
    nueva_pelicula = {
        'id': obtener_nuevo_id(),
        'titulo': request.json['titulo'],
        'genero': request.json['genero']
    }
    peliculas.append(nueva_pelicula)
    print(peliculas)

def actualizar_pelicula(id):
    # Lógica para buscar la película por su ID y actualizar sus detalles
    # Se considera un nuevo bloque que "pise" el bloque anterior directamente en lugar de reemplazar los valores 
    pelicula_actualizada = {
        "id": id,
        "titulo": request.json["titulo"],
        "genero": request.json["genero"]
    }
    peliculas[id] = pelicula_actualizada
    return jsonify(pelicula_actualizada)


def eliminar_pelicula(id):
    # Lógica para buscar la película por su ID y eliminarla
    # Considerando que al eliminar un bloque (de tipo diccionario) de la lista, no se modifican los demas elementos. Es decir, queda como un "hueco" con respecto a los IDs
    # Por eso mismo no podemos usar simplemente la funcion de lista que elimina el elemento que queremos 
    # (list.remove(x) // esta funcion cambiaria los IDs y por tanto, alteraria las otras funciones
    peliculas[id] = "Pelicula no encontrada"
    return jsonify({'mensaje': 'Película eliminada correctamente'})


def obtener_nuevo_id():
    if len(peliculas) > 0:
        ultimo_id = peliculas[-1]['id']
        return ultimo_id + 1
    else:
        return 1

def feriado_recomendacion(genero):
    # Obtenemos proximo feriado
    next_holiday = NextHoliday()
    next_holiday.fetch_holidays(holiday_type=None)
    holiday = next_holiday.ret_date()
    #map = {
    #    "Ciencia-ficcion": "Ciencia ficción",
    #    "Accion": "Acción",
    #    "Fantasia": "Fantasía",
    #}
    # llamamos funcion para normalizar los nombres de los generos (debido a la url)
    map = normalize_genres()
    # obtenemos el genero particular que seleccionamos
    genero = map.get(genero, genero)
    # obtenemos la pelicula con el genero seleccionado
    p_titulos = [pelicula.get("titulo") for pelicula in peliculas if pelicula.get("genero") == genero]
    # seleccionamos una pelicula randomizada de entre todas con el genero seleccionado
    p_titulo = random.choice(p_titulos)
    return jsonify({
        'prox_feriado': f"{holiday['dia']}/{holiday['mes']}",
        'motivo': (holiday['motivo']),
        'titulo': p_titulo}
        )

def normalize_genres():
    special_characters ={
      'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
      'ñ': 'n', 'Ñ': 'N', 'ü': 'u', ' ': '-',
      'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
      'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
      'Ä': 'A', 'Ë': 'E', 'Ï': 'I', 'Ö': 'O', 'Ü': 'U',
    }
    temp = set()

    # Agregamos todos los generos disponibles
    for pelicula in peliculas:
        temp.add(pelicula['genero'])

    genre_map = {}

    # Normalizamos los generos
    for item in temp:
        normalized_genre = item.translate(str.maketrans(special_characters))
        genre_map[normalized_genre] = item

    return genre_map
    
app.add_url_rule('/peliculas', 'obtener_peliculas', obtener_peliculas, methods=['GET'])
app.add_url_rule('/peliculas/<int:id>', 'obtener_pelicula', obtener_pelicula, methods=['GET'])
app.add_url_rule('/peliculas/recomendacion/<string:genero>', 'feriado_recomendacion', feriado_recomendacion, methods=['GET'])
app.add_url_rule('/peliculas', 'agregar_pelicula', agregar_pelicula, methods=['POST'])
app.add_url_rule('/peliculas/<int:id>', 'actualizar_pelicula', actualizar_pelicula, methods=['PUT'])
app.add_url_rule('/peliculas/<int:id>', 'eliminar_pelicula', eliminar_pelicula, methods=['DELETE'])

if __name__ == '__main__':
    app.run()
