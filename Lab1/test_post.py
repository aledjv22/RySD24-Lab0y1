import requests

def post_test():
  print("--------------------------------------")
  print("Inicio de las pruebas del método POST.")
  print("--------------------------------------")

  # Agregar una nueva película
  ## Respuesta correcta (201)
  print("-----------------------------------------------------")
  print("Agregar una nueva película. Respuesta correcta [201].")
  print("-----------------------------------------------------")
  peliculas = [
    { 'titulo': 'The Super Mario Bros.', 'genero': 'Infantil'},
    { 'titulo': 'El niño y la garza', 'genero': 'Fantasía'},
    { 'titulo': 'Shang-Chi and the Legend of the Ten Rings', 'genero': 'Acción'},
    { 'titulo': 'Fantastic Beasts and Where to Find Them', 'genero': 'Fantasía'}
  ]
  for pelicula in peliculas:
    response = requests.post('http://localhost:5000/peliculas', json=pelicula)
    if response.status_code == 201:
      pelicula_agregada = response.json()
      print("Película agregada:")
      print(f"Título: {pelicula_agregada['titulo']}, Género: {pelicula_agregada['genero']}")
    else:
      print("Error al agregar la película.")
    print()
  
  ## Respuesta incorrecta (400)
  print()
  print("-------------------------------------------------------")
  print("Agregar una nueva película. Respuesta incorrecta [400].")
  print("-------------------------------------------------------")
  peliculas = [
    { 'titulo': 'The Super Mario Bros.', 'genero': ''},
    { 'titulo': 23, 'genero': 'Fantasía'},
    { 'titulo': '', 'genero': ''},
    { 'titulo': 'Shang-Chi and the Legend of the Ten Rings', 'genero': 'Acción'}
  ]
  for pelicula in peliculas:
    response = requests.post('http://localhost:5000/peliculas', json=pelicula)
    if response.status_code == 400:
      print(f"Error captado de forma correcta, falta de datos de la película o datos incorrectos.")
    else:
      print(f"ERROR, si se agrego la pelicula, se obtubo {response.status_code} en lugar de 400.")
      pelicula_agregada = response.json()
      print("Película agregada:")
      print(f"Título: {pelicula_agregada['titulo']}, Género: {pelicula_agregada['genero']}")
    print()