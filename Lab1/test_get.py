import requests

def get_test():
  print("=====================================")
  print("Inicio de las pruebas del método GET.")
  print("=====================================")

  # Obtener todas las películas
  print("------------------------------------------------------")
  print("Obtener todas las películas. Respuesta correcta [200].")
  print("------------------------------------------------------")
  response = requests.get('http://localhost:5000/peliculas')
  if response.status_code == 200:
      peliculas = response.json()
      print("Películas:")
      for pelicula in peliculas:
          print(f"ID: {pelicula['id']}, Título: {pelicula['titulo']}, Género: {pelicula['genero']}")
  elif response.status_code == 404:
      print("No hay películas registradas.")
  else:
      print(f"Error al obtener las películas. Código de estado: {response.status_code}")
  print()


  # Obtener detalles de una película específica
  ## Respuesta correcta  (200)
  print("----------------------------------------------------------------------")
  print("Obtener detalles de una película específica. Respuesta correcta [200].")
  print("----------------------------------------------------------------------")
  id_peliculas = [1, 2, 3, 4]  # Lista de IDs de películas a obtener
  for id_pelicula in id_peliculas:
    response = requests.get(f'http://localhost:5000/peliculas/{id_pelicula}')
    if response.status_code == 200:
      pelicula = response.json()
      print("Detalles de la película:")
      print(f"ID: {pelicula['id']}, Título: {pelicula['titulo']}, Género: {pelicula['genero']}")
    elif response.status_code == 404:
      print(f"Película con ID {id_pelicula} no encontrada.")
    else:
      print("Error al obtener los detalles de la película.")
    print()

  ## Respuesta incorrecta (404)
  print("------------------------------------------------------------------------")
  print("Obtener detalles de una película específica. Respuesta incorrecta [404].")
  print("------------------------------------------------------------------------")
  id_peliculas = [-21, 210290132, 'ALE', '-ˀ2']  # Lista de IDs de películas a obtener
  for id_pelicula in id_peliculas:
    response = requests.get(f'http://localhost:5000/peliculas/{id_pelicula}')
    if response.status_code == 404:
        print(f"Error captado de forma correcta, {id_pelicula} no es un ID correcto. ")
    elif response.status_code == 200:
        print(f"ERROR GRAVE, se obtuvo una respuesta de 200 en lugar de 404.")
        pelicula = response.json()
        print("Detalles de la película:")
        print(f"ID: {pelicula['id']}, Título: {pelicula['titulo']}, Género: {pelicula['genero']}")
    else:
        print(f"ERROR, si se obtuvo una respuesta diferente a 404, se obtuvo {response.status_code}")
    print()


  # Obtener peliculas por un genero
  ## Respuesta correcta  (200)
  print()
  print("-------------------------------------------------------")
  print("Obtener películas por género. Respuesta correcta [200].")
  print("-------------------------------------------------------")
  generos = ['ciencia_ficcion', 'comedia', 'drama', 'terror']  # Lista de géneros de películas a obtener
  for genero in generos:
    response = requests.get(f'http://localhost:5000/peliculas/genero/{genero}')
    if response.status_code == 200:
      peliculas = response.json()
      print(f"Películas por género {genero}:")
      for pelicula in peliculas:
        print(f"ID: {pelicula['id']}, Título: {pelicula['titulo']}, Género: {pelicula['genero']}")
    elif response.status_code == 404:
      print(f"No hay películas de género {genero}.")
    else:
      print("Error al obtener las películas por género.")
    print()

  ## Respuesta incorrecta (400)
  print("---------------------------------------------------------")
  print("Obtener películas por género. Respuesta incorrecta [400].")
  print("---------------------------------------------------------")
  generos = [233213, 'pepe pepa', 'ale diaz', -5]  # Lista de géneros de películas a obtener
  for genero in generos:
    response = requests.get(f'http://localhost:5000/peliculas/genero/{genero}')
    if response.status_code == 400:
        print(f"Error captado de forma correcta, no hay películas de género {genero}.")
    elif response.status_code == 200:
        print(f"ERROR GRAVE, se obtuvo una respuesta de 200 en lugar de 400.")
        peliculas = response.json()
        print(f"Películas por género {genero}:")
        for pelicula in peliculas:
          print(f"ID: {pelicula['id']}, Título: {pelicula['titulo']}, Género: {pelicula['genero']}")
    else:
        print(f"ERROR, si se obtuvo una respuesta diferente a 400, se obtuvo {response.status_code}")
    print()


  # Obtener peliculas por titulo
  ## Respuesta correcta  (200)
  print()
  print("------------------------------------------------------")
  print("Buscar películas por título. Respuesta correcta [200].")
  print("------------------------------------------------------")
  titulos = ['Max', 'the', 'club', 'to']  # Lista de títulos de películas a buscar
  for titulo in titulos:
    response = requests.get(f'http://localhost:5000/peliculas/buscar/{titulo}')
    if response.status_code == 200:
      peliculas = response.json()
      print(f"Películas por título {titulo}:")
      for pelicula in peliculas:
        print(f"ID: {pelicula['id']}, Título: {pelicula['titulo']}, Género: {pelicula['genero']}")
    elif response.status_code == 404:
      print(f"No hay películas con título {titulo}.")
    else:
      print("Error al buscar las películas por título.")
    print()

  ## Respuesta incorrecta (400)
  print("--------------------------------------------------------")
  print("Buscar películas por título. Respuesta incorrecta [400].")
  print("--------------------------------------------------------")
  titulos = [233213, 'pepe pepa', 'ale diaz', -5]  # Lista de títulos de películas a buscar
  for titulo in titulos:
    response = requests.get(f'http://localhost:5000/peliculas/buscar/{titulo}')
    if response.status_code == 400:
        print(f"Error captado de forma correcta, no hay películas con título {titulo}.")
    elif response.status_code == 200:
        print(f"ERROR GRAVE, se obtuvo una respuesta de 200 en lugar de 400.")
        peliculas = response.json()
        print(f"Películas por título {titulo}:")
        for pelicula in peliculas:
          print(f"ID: {pelicula['id']}, Título: {pelicula['titulo']}, Género: {pelicula['genero']}")
    else:
        print(f"ERROR, si se obtuvo una respuesta diferente a 400, se obtuvo {response.status_code}")
    print()

  # Obtener una pelicula random sugerida
  ## Respuesta correcta  (200)
  print()
  print("----------------------------------------------------------------")
  print("Obtener una película sugerida al azar. Respuesta correcta [200].")
  print("----------------------------------------------------------------")
  for _ in range(5):
    response = requests.get('http://localhost:5000/peliculas/sugerir')
    if response.status_code == 200:
      pelicula_sugerida = response.json()
      print("Película sugerida:")
      print(f"ID: {pelicula_sugerida['id']}, Título: {pelicula_sugerida['titulo']}, Género: {pelicula_sugerida['genero']}")
    elif response.status_code == 404:
      print("No hay películas para sugerir.")
    else:
      print("Error al obtener la película sugerida.")


  # Obtener una pelicula random sugerida por genero
  ## Respuesta correcta  (200)
  print()
  print("---------------------------------------------------------------------------")
  print("Obtener una película sugerida al azar por género. Respuesta correcta [200].")
  print("---------------------------------------------------------------------------")
  generos = ['accion', 'comedia', 'drama', 'terror']  # Lista de géneros de películas a sugerir
  for genero in generos:
    response = requests.get(f'http://localhost:5000/peliculas/sugerir/{genero}')
    if response.status_code == 200:
      pelicula_sugerida = response.json()
      print(f"Película sugerida de género {genero}:")
      print(f"ID: {pelicula_sugerida['id']}, Título: {pelicula_sugerida['titulo']}, Género: {pelicula_sugerida['genero']}")
    elif response.status_code == 404:
      print(f"No hay películas de género {genero} para sugerir.")
    else:
      print("Error al obtener la película sugerida.")
    print()

  ## Respuesta incorrecta (400)
  print("-----------------------------------------------------------------------------")
  print("Obtener una película sugerida al azar por género. Respuesta incorrecta [400].")
  print("-----------------------------------------------------------------------------")
  generos = [233213, 'pepe pepa', 'ale diaz', -5]  # Lista de géneros de películas a sugerir
  for genero in generos:
    response = requests.get(f'http://localhost:5000/peliculas/sugerir/{genero}')
    if response.status_code == 400:
        print(f"Error captado de forma correcta, no hay películas de género {genero} para sugerir.")
    elif response.status_code == 200:
        print(f"ERROR GRAVE, se obtuvo una respuesta de 200 en lugar de 400.")
        pelicula_sugerida = response.json()
        print(f"Película sugerida de género {genero}:")
        print(f"ID: {pelicula_sugerida['id']}, Título: {pelicula_sugerida['titulo']}, Género: {pelicula_sugerida['genero']}")
    else:
        print(f"ERROR, si se obtuvo una respuesta diferente a 400, se obtuvo {response.status_code}")
    print()


  # Obtener una pelicula random sugerida por genero indicando el proximo feriado
  ## Respuesta correcta  (200)
  print()
  print("---------------------------------------------------")
  print("Película al azar por el género indicando mostrando")
  print("el próximo feriado. Respuesta correcta [200].")
  print("---------------------------------------------------")
  generos = ['accion', 'comedia', 'drama', 'terror']  # Lista de géneros de películas a sugerir
  for genero in generos:
    response = requests.get(f'http://localhost:5000/peliculas/recomendacion/{genero}')
    if response.status_code == 200:
      recomendacion = response.json()
      print(f"Recomendación de película de género {genero}:")
      print(f"Próximo feriado: {recomendacion['prox_feriado']}")
      print(f"Motivo del feriado: {recomendacion['motivo']}")
      print(f"Película recomendada: {recomendacion['titulo']}")
    elif response.status_code == 404:
      print(f"No hay películas de género {genero} para sugerir.")
    else:
      print("Error al obtener la película sugerida.")
    print()

  ## Respuesta incorrecta (400)
  print("---------------------------------------------------")
  print("Película al azar por el género indicando mostrando")
  print("el próximo feriado. Respuesta incorrecta [400].")
  print("---------------------------------------------------")
  generos = [233213, 'pepe pepa', 'ale diaz', -5]  # Lista de géneros de películas a sugerir
  for genero in generos:
    response = requests.get(f'http://localhost:5000/peliculas/recomendacion/{genero}')
    if response.status_code == 400:
        print(f"Error captado de forma correcta, no hay películas de género {genero} para sugerir.")
    elif response.status_code == 200:
        print(f"ERROR GRAVE, se obtuvo una respuesta de 200 en lugar de 400.")
        recomendacion = response.json()
        print(f"Recomendación de película de género {genero}:")
        print(f"Próximo feriado: {recomendacion['prox_feriado']}")
        print(f"Motivo del feriado: {recomendacion['motivo']}")
        print(f"Película recomendada: {recomendacion['titulo']}")
    else:
        print(f"ERROR, si se obtuvo una respuesta diferente a 400, se obtuvo {response.status_code}")
    print()

  print("==================================")
  print("Fin de las pruebas del método GET.")
  print("==================================")
  print()