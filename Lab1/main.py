import random
from flask import Flask, jsonify, request
from proximo_feriado import NextHoliday
from unidecode import unidecode
from pelis import peliculas

app = Flask(__name__)



def obtener_peliculas():
    return jsonify(peliculas)


# Buscar la película por su ID
def obtener_pelicula(id):
    pelicula_encontrada = None
    for pelicula in peliculas:
        if pelicula['id'] == id:
            pelicula_encontrada = pelicula
            break
    # Si no se encontró la película, devolver un mensaje
    if (pelicula_encontrada is None):
        return jsonify({'mensaje': 'Pelicula no encontrada.'}), 404
    # Si se encontró la película, devolver sus detalles y el código de estado 200 (OK)
    return jsonify(pelicula_encontrada), 200


# Normalizar el texto de entrada
def normalize_input(input_string):
    input_string = input_string.lower()
    input_string = input_string.replace(" ", "_")
    input_string = unidecode(input_string)

    return input_string


# Lógica para agregar una nueva película
def agregar_pelicula():
    nueva_pelicula = {
        'id': obtener_nuevo_id(),
        'titulo': request.json['titulo'],
        'genero': request.json['genero']
    }
    # Validar que se hayan ingresado los datos de la película
    if nueva_pelicula['titulo'] == "" or nueva_pelicula['genero'] == "":
        return jsonify({'mensaje': 'Faltan datos de la película'}), 400
    peliculas.append(nueva_pelicula)
    # Devolver los detalles de la nueva película y el código de estado 201 (creado)
    return jsonify(nueva_pelicula), 201


# Lógica para buscar la película por su ID y actualizar sus detalles
def actualizar_pelicula(id):
    pelicula_actualizada = {
        "id": id,
        "titulo": request.json["titulo"],
        "genero": request.json["genero"]
    }
    # Validar que se hayan ingresado los datos de la película
    if pelicula_actualizada['titulo'] == "" or pelicula_actualizada['genero'] == "":
        return jsonify({'mensaje': 'Faltan datos de la película'}), 400
    # Nueva lista de películas sin la película que quiero actualizar
    peliculas_menos_id = [pelicula for pelicula in peliculas if pelicula['id'] != id]
    # Se incluye la película actualizada en la nueva lista
    peliculas_menos_id.append(pelicula_actualizada)
    # Se reemplaza la lista original por la nueva
    peliculas.clear()
    peliculas.extend(peliculas_menos_id)
    # Devolver los detalles de la película actualizada y el código de estado 200 (OK)
    return jsonify(pelicula_actualizada), 200


# Lógica para buscar la película por su ID y eliminarla
def eliminar_pelicula(id):
    # Validar que la película exista
    if not any(pelicula['id'] == id for pelicula in peliculas):
        return jsonify({'mensaje': 'Pelicula no encontrada.'}), 404
    # Nueva lista de películas sin la película que quiero eliminar
    peliculas_menos_id = [pelicula for pelicula in peliculas if pelicula['id'] != id]
    # Se reemplaza la lista original por la nueva
    peliculas.clear()
    peliculas.extend(peliculas_menos_id)
    # Devolver un mensaje de confirmación de eliminación de la película y el código de estado 200 (OK)
    return jsonify({'mensaje': 'Película eliminada correctamente'}), 200


# Lógica para obtener las películas por género
def obtener_peliculas_por_genero(genero):
    # Validar que se haya ingresado el género de la película
    if genero == "":
        return jsonify({'mensaje': 'Falta el género de la película.'}), 400
    # Normalizar el género de entrada
    genero = normalize_input(genero)
    # Filtrado de la lista de películas por género
    peliculas_filtradas = [pelicula for pelicula in peliculas if genero == normalize_input(pelicula['genero'])]
    # Devolver la lista de películas filtradas por género y el código de estado 200 (OK)
    return jsonify(peliculas_filtradas), 200


# Lógica para buscar películas por título
def buscar_peliculas(titulo):
    # Validar que se haya ingresado el título de la película
    if titulo == "":
        return jsonify({'mensaje': 'Falta el título de la película.'}), 400
    # Normalizar el título de entrada
    titulo = normalize_input(titulo)
    # Filtrado de la lista de películas por título
    peliculas_filtradas = [pelicula for pelicula in peliculas if titulo in normalize_input(pelicula['titulo'])]
    # Devolver la lista de películas filtradas por título y el código de estado 200 (OK)
    return jsonify(peliculas_filtradas), 200


# Lógica para sugerir una película al azar
def sugerir_pelicula():
    # Seleccionar una película al azar de la lista de películas
    pelicula_sugerida = random.choice(peliculas)
    # Validar que haya películas en la lista
    if not pelicula_sugerida:
        return jsonify({'mensaje': 'No hay películas para sugerir.'}), 404
    # Devolver los detalles de la película sugerida y el código de estado 200 (OK)
    return jsonify(pelicula_sugerida), 200


# Lógica para sugerir una película al azar por género
def sugerir_pelicula_por_genero(genero):
    # Validar que se haya ingresado el género de la película
    if genero == "":
        return jsonify({'mensaje': 'Falta el género de la película.'}), 400
    # Normalizar el género de entrada
    genero = normalize_input(genero)
    # Filtrado de la lista de películas por género
    peliculas_filtradas = [pelicula for pelicula in peliculas if genero == normalize_input(pelicula['genero'])]
    # Seleccionar una película al azar de la lista de películas filtradas
    pelicula_sugerida = random.choice(peliculas_filtradas)
    # Validar que haya películas en la lista filtrada, devolver los 
    # detalles de la película sugerida y el código de estado 200 (OK)
    return jsonify(pelicula_sugerida), 200

# Lógica para obtener un nuevo ID
def obtener_nuevo_id():
    if len(peliculas) > 0:
        ultimo_id = peliculas[-1]['id']
        return ultimo_id + 1
    else:
        return 1


# Lógica para obtener una recomendación de película para el próximo feriado
def feriado_recomendacion(genero):
    # Validar que se haya ingresado el género de la película
    if genero == "":
        return jsonify({'mensaje': 'Falta el género de la película.'}), 400
    # Obtenemos el próximo feriado
    next_holiday = NextHoliday()
    next_holiday.fetch_holidays()
    # obtenemos la pelicula con el genero seleccionado
    p_titulos = [pelicula.get("titulo") for pelicula in peliculas if pelicula.get("genero") == genero]
    # seleccionamos una pelicula randomizada de entre todas con el genero seleccionado
    p_titulo = random.choice(p_titulos)
    # Devolver los detalles de la película recomendada y el código de estado 200 (OK)
    return jsonify({
        'prox_feriado': f"{next_holiday.holiday['dia']}/{next_holiday.holiday['mes']}",
        'motivo': (next_holiday.holiday['motivo']),
        'titulo': p_titulo}), 200


# Rutas de la API
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
