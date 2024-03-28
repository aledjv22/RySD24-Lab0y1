import requests
import pytest
import requests_mock

@pytest.fixture
def mock_response():
    with requests_mock.Mocker() as m:
        # Simulamos la respuesta para obtener todas las películas
        m.get('http://localhost:5000/peliculas', json=[
            {'id': 1, 'titulo': 'Indiana Jones', 'genero': 'Acción'},
            {'id': 2, 'titulo': 'Star Wars', 'genero': 'Acción'}
        ])

        # Simulamos la respuesta para agregar una nueva película
        m.post('http://localhost:5000/peliculas', status_code=201, json={'id': 3, 'titulo': 'Pelicula de prueba', 'genero': 'Acción'})

        # Simulamos la respuesta para obtener detalles de una película específica
        m.get('http://localhost:5000/peliculas/1', json={'id': 1, 'titulo': 'Indiana Jones', 'genero': 'Acción'})

        # Simulamos la respuesta para actualizar los detalles de una película
        m.put('http://localhost:5000/peliculas/1', status_code=200, json={'id': 1, 'titulo': 'Nuevo título', 'genero': 'Comedia'})

        # Simulamos la respuesta para eliminar una película
        m.delete('http://localhost:5000/peliculas/1', status_code=200)

        # Simulamos la respuesta para obtener recomendacion de pelicula para feriado por genero
        m.get('http://localhost:5000/peliculas/recomendacion/drama', status_code=200)
        m.get('http://localhost:5000/peliculas/recomendacion/ciencia_ficcion', status_code=200)
        m.get('http://localhost:5000/peliculas/recomendacion/Ciencia ficción', status_code=400)

        # Simulamos la respuesta para obtener sugerencia de pelicula por genero
        m.get('http://localhost:5000/peliculas/sugerir/drama', status_code=200)
        m.get('http://localhost:5000/peliculas/sugerir/ciencia_ficcion', status_code=200)
        m.get('http://localhost:5000/peliculas/sugerir/Ciencia ficción', status_code=400)

        # Simulamos la respuesta para obtener sugerencia de pelicula
        m.get('http://localhost:5000/peliculas/sugerir', status_code=200)

        # Simulamos la respuesta para obtener pelicula por titulo
        m.get('http://localhost:5000/peliculas/buscar/The', status_code=200)

        # Simulamos la respuesta para obtener pelicula por genero
        m.get('http://localhost:5000/peliculas/genero/drama', status_code=200)

        yield m

def test_obtener_peliculas(mock_response):
    response = requests.get('http://localhost:5000/peliculas')
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_agregar_pelicula(mock_response):
    nueva_pelicula = {'titulo': 'Pelicula de prueba', 'genero': 'Acción'}
    response = requests.post('http://localhost:5000/peliculas', json=nueva_pelicula)
    assert response.status_code == 201
    assert response.json()['id'] == 3

def test_obtener_detalle_pelicula(mock_response):
    response = requests.get('http://localhost:5000/peliculas/1')
    assert response.status_code == 200
    assert response.json()['titulo'] == 'Indiana Jones'

def test_actualizar_detalle_pelicula(mock_response):
    datos_actualizados = {'titulo': 'Nuevo título', 'genero': 'Comedia'}
    response = requests.put('http://localhost:5000/peliculas/1', json=datos_actualizados)
    assert response.status_code == 200
    assert response.json()['titulo'] == 'Nuevo título'

def test_eliminar_pelicula(mock_response):
    response = requests.delete('http://localhost:5000/peliculas/1')
    assert response.status_code == 200

def test_feriado_recomendacion(mock_response):
    response = requests.get('http://localhost:5000/peliculas/recomendacion/drama')
    assert response.status_code == 200

def test_feriado_recomendacion2(mock_response):
    response = requests.get('http://localhost:5000/peliculas/recomendacion/ciencia_ficcion')
    assert response.status_code == 200

def test_feriado_recomendacion3(mock_response):
    response = requests.get('http://localhost:5000/peliculas/recomendacion/Ciencia ficción')
    assert response.status_code == 400

def sugerir_pelicula_por_genero(mock_response):
    response = requests.get('http://localhost:5000/peliculas/sugerir/drama')
    assert response.status_code == 200

def sugerir_pelicula_por_genero2(mock_response):
    response = requests.get('http://localhost:5000/peliculas/sugerir/ciencia_ficcion')
    assert response.status_code == 200

def sugerir_pelicula_por_genero3(mock_response):
    response = requests.get('http://localhost:5000/peliculas/sugerir/Ciencia ficción')
    assert response.status_code == 400

def sugerir_pelicula(mock_response):
    response = requests.get('http://localhost:5000/peliculas/sugerir')
    assert response.status_code == 200

def buscar_peliculas(mock_response):
    response = requests.get('http://localhost:5000/peliculas/buscar/The')
    assert response.status_code == 200

def obtener_peliculas_por_genero(mock_response):
    response = requests.get('http://localhost:5000/peliculas/genero/drama')
    assert response.status_code == 200

