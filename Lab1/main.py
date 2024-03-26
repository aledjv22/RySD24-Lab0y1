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
    # Buscar la película por su ID
    pelicula_encontrada = None
    for pelicula in peliculas:
        if pelicula['id'] == id:
            pelicula_encontrada = pelicula
            break

    return jsonify(pelicula_encontrada)


def agregar_pelicula():
    nueva_pelicula = {
        'id': obtener_nuevo_id(),
        'titulo': request.json['titulo'],
        'genero': request.json['genero']
    }
    peliculas.append(nueva_pelicula)
    print(peliculas)
    return jsonify(nueva_pelicula), 201

def actualizar_pelicula(id):
    # Lógica para buscar la película por su ID y actualizar sus detalles
    pelicula_actualizada = {
        "id": id,
        "titulo": request.json["titulo"],
        "genero": request.json["genero"]
    }
    # Genero una nueva lista omitiendo la pelicula con el id que quiero actualizar
    peliculas_menos_id = [pelicula for pelicula in peliculas if pelicula['id'] != id]
    # Agrego la pelicula actualizada a la lista nueva
    peliculas_menos_id.append(pelicula_actualizada)
    # Elimino la lista original y la reemplazo por la nueva
    peliculas.clear()
    peliculas.extend(peliculas_menos_id)

    return jsonify(pelicula_actualizada)


def eliminar_pelicula(id):
    # Genero una nueva lista omitiendo la pelicula con el id que quiero eliminar
    peliculas_menos_id = [pelicula for pelicula in peliculas if pelicula['id'] != id]
    # Elimino la lista original y la reemplazo por la nueva
    peliculas.clear()
    peliculas.extend(peliculas_menos_id)

    return jsonify({'mensaje': 'Película eliminada correctamente'})


def obtener_peliculas_por_genero(genero):
    # Filtro la lista de películas por género
    peliculas_filtradas = [pelicula for pelicula in peliculas if pelicula['genero'] == genero]

    return jsonify(peliculas_filtradas)


def buscar_peliculas(titulo):
    # Filtro la lista de películas por título
    peliculas_filtradas = [pelicula for pelicula in peliculas if titulo.lower() in pelicula['titulo'].lower()]

    return jsonify(peliculas_filtradas)


def sugerir_pelicula():
    # Selecciono una película al azar de la lista de películas
    pelicula_sugerida = random.choice(peliculas)

    return jsonify(pelicula_sugerida)


def sugerir_pelicula_por_genero(genero):
    # Filtro la lista de películas por género
    peliculas_filtradas = [pelicula for pelicula in peliculas if pelicula['genero'] == genero]
    # Selecciono una película al azar de la lista de películas filtradas
    pelicula_sugerida = random.choice(peliculas_filtradas)

    return jsonify(pelicula_sugerida)


def obtener_nuevo_id():
    if len(peliculas) > 0:
        ultimo_id = peliculas[-1]['id']
        return ultimo_id + 1
    else:
        return 1

def feriado_recomendacion(genero):
    # Obtenemos proximo feriado
    next_holiday = NextHoliday()
    next_holiday.fetch_holidays()

    # Siguiente si se quiere utilizar Curl correctamente, ademas descomentar normalize_genres()
    """ llamamos funcion para normalizar los nombres de los generos (debido a la url)
     map = normalize_genres()

     obtenemos el genero particular que seleccionamos
     genero = map.get(genero, genero)"""

    # obtenemos la pelicula con el genero seleccionado
    p_titulos = [pelicula.get("titulo") for pelicula in peliculas if pelicula.get("genero") == genero]
    # seleccionamos una pelicula randomizada de entre todas con el genero seleccionado
    p_titulo = random.choice(p_titulos)
    return jsonify({
        'prox_feriado': f"{next_holiday.holiday['dia']}/{next_holiday.holiday['mes']}",
        'motivo': (next_holiday.holiday['motivo']),
        'titulo': p_titulo}
        )

"""def normalize_genres():
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

    return genre_map"""



app.add_url_rule('/peliculas', 'obtener_peliculas', obtener_peliculas, methods=['GET'])
app.add_url_rule('/peliculas/<int:id>', 'obtener_pelicula', obtener_pelicula, methods=['GET'])
app.add_url_rule('/peliculas/genero/<string:genero>', 'obtener_peliculas_por_genero', obtener_peliculas_por_genero, methods=['GET'])
app.add_url_rule('/peliculas/buscar/<string:titulo>', 'buscar_peliculas', buscar_peliculas, methods=['GET'])
app.add_url_rule('/peliculas/sugerir', 'sugerir_pelicula', sugerir_pelicula, methods=['GET'])
app.add_url_rule('/peliculas/sugerir/<string:genero>', 'sugerir_pelicula_por_genero', sugerir_pelicula_por_genero, methods=['GET'])
app.add_url_rule('/peliculas/recomendacion/<string:genero>', 'feriado_recomendacion', feriado_recomendacion, methods=['GET'])
app.add_url_rule('/peliculas', 'agregar_pelicula', agregar_pelicula, methods=['POST'])
app.add_url_rule('/peliculas/<int:id>', 'actualizar_pelicula', actualizar_pelicula, methods=['PUT'])
app.add_url_rule('/peliculas/<int:id>', 'eliminar_pelicula', eliminar_pelicula, methods=['DELETE'])

if __name__ == '__main__':
    app.run()
