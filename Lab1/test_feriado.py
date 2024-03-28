from proximo_feriado import NextHoliday

def feriado_test():
    print()
    print("========================================")
    print("Inicio de las pruebas de la API de feriados.")
    print("========================================")
    # Sin Parametro tipo
    ## Respuesta correcta (200)
    print("------------------------------------------------")
    print("Proximo feriado sin parametro tipo")
    print("------------------------------------------------")
    next_holiday = NextHoliday()
    proximo = next_holiday.fetch_holidays()
    
      print(f"Película ID: {id_pelicula} eliminada correctamente.")
    else:
      print("Error al eliminar la película.")
    print()

  ## Respuesta incorrecta (404)
  print("--------------------------------------------------")
  print("Eliminar una película. Respuesta incorrecta [404].")
  print("--------------------------------------------------")
  id_peliculas = [1, 2, -3, 'pepe']
  for id_pelicula in id_peliculas:
    response = requests.delete(f'http://localhost:5000/peliculas/{id_pelicula}')
    if response.status_code == 404:
      print(f"Error captado de forma correcta, la película con ID {id_pelicula} no existe.")
    else:
      print(f"ERROR, si se elimino la pelicula, se obtubo {response.status_code} en lugar de 404.")
    print()