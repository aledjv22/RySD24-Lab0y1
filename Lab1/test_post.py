import requests

def post_test():
  print()
  print("======================================")
  print("Inicio de las pruebas del método POST.")
  print("======================================")

  # Agregar una nueva película
  ## Respuesta correcta (201)
  print("-----------------------------------------------------")
  print("Agregar una nueva película. Respuesta correcta [201].")
  print("-----------------------------------------------------")
  peliculas = [
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
  print("-------------------------------------------------------")
  print("Agregar una nueva película. Respuesta incorrecta [400].")
  print("-------------------------------------------------------")
  peliculas = [
    { 'titulo': 'The Super Mario Bros.', 'genero': ''},
    { 'titulo': '', 'genero': 'Fantasía'},
    { 'titulo': '', 'genero': ''}
  ]
  for pelicula in peliculas:
    response = requests.post('http://localhost:5000/peliculas', json=pelicula)
    if response.status_code == 400:
      print("Error captado de forma correcta, falta de datos de la película.")
    elif response.status_code == 201:
      print(f"ERROR GRAVE, se agrego la pelicula y se obtuvo {response.status_code} en lugar de 400.")
      pelicula_agregada = response.json()
      print("Película agregada:")
      print(f"Título: {pelicula_agregada['titulo']}, Género: {pelicula_agregada['genero']}")
    else:
      print(f"ERROR, se obtuvo {response.status_code} en lugar de 400.")
    print()