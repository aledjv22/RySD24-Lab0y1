import requests

def put_test():
  print()
  print("=====================================")
  print("Inicio de las pruebas del método PUT.")
  print("=====================================")

  # Actualizar los detalles de una película
  ## Respuesta correcta (200)
  print("--------------------------------------------------")
  print("Actualizar una película. Respuesta correcta [200].")
  print("--------------------------------------------------")
  peliculas = [
    { 'id': 1, 'titulo': 'Indiana Jones', 'genero': 'Aventura' },
    { 'id': 2, 'titulo': 'La guerra de las galaxias', 'genero': 'Ciencia ficción' },
    { 'id': 3, 'titulo': 'Interestelar', 'genero': 'Ciencia ficción' }
  ]
  for pelicula in peliculas:
    response = requests.put(f'http://localhost:5000/peliculas/{pelicula["id"]}', json=pelicula)
    if response.status_code == 200:
      pelicula_actualizada = response.json()
      print("Película actualizada:")
      print(f"ID: {pelicula_actualizada['id']}, Título: {pelicula_actualizada['titulo']}, Género: {pelicula_actualizada['genero']}")
    else:
      print("Error al actualizar la película.")
    print()

  ## Respuesta incorrecta (400 y 404)
  print("------------------------------------------------------------")
  print("Actualizar una película. Respuesta incorrecta [400] y [404].")
  print("------------------------------------------------------------")
  peliculas = [
    { 'id': 1, 'titulo': 'Indiana Jones', 'genero': '' },
    { 'id': 2, 'titulo': '', 'genero': 'Ciencia ficción' },
    { 'id': 3, 'titulo': '', 'genero': '' },
    { 'id': -32, 'titulo': 'Jurassic Park', 'genero': 'Aventura'},
    {'id': 'pepe', 'titulo': 'The Avengers', 'genero': 'Acción'}
  ]
  for pelicula in peliculas:
    response = requests.put(f'http://localhost:5000/peliculas/{pelicula["id"]}', json=pelicula)
    if response.status_code == 404:
      print(f"Error captado de forma correcta, la película con ID {pelicula['id']} no existe.")
    elif response.status_code == 400:
      print(f"Error captado de forma correcta, falta de datos de la película.")
    elif response.status_code == 200:
      print(f"ERROR, si se actualizo la pelicula, se obtuvo {response.status_code} en lugar de 400 o 404.")
      pelicula_actualizada = response.json()
      print("Película actualizada:")
      print(f"ID: {pelicula_actualizada['id']}, Título: {pelicula_actualizada['titulo']}, Género: {pelicula_actualizada['genero']}")
    else:
      print(f"ERROR, se obtubo {response.status_code} en lugar de 400 o 404.")
    print()