#!/bin/bash

# Definir la URL base:
localhost="http://localhost:5000"

# Colores
green='\033[0;32m'
red='\033[0;31m'
yellow='\033[1;33m'
cyan='\033[0;36m'
blue='\033[0;34m'
NC='\033[0m' # No Color

# Inicio de pruebas del metodo GET:
echo -e "${yellow}=================================="
echo "Inicio de pruebas del metodo GET."
echo "=================================="
echo ""

# Obtener todas las peliculas:
echo -e "${green}------------------------------------------------------"
echo "Obtener todas las peliculas. Respuesta correcta [200]."
echo -e "------------------------------------------------------${NC}"
curl_request="curl -s "$localhost/peliculas""
echo -e "Consulta realizada: ${cyan}$curl_request"
$curl_request > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json
echo ""

# Obtener detalles de una pelicula especifica:
## Respuesta correcta [200].
echo -e "${green}----------------------------------------------------------------------"
echo "Obtener detalles de una pelicula especifica. Respuesta correcta [200]."
echo -e "----------------------------------------------------------------------${NC}"
curl_request="curl -s "$localhost/peliculas/8""
echo -e "Consulta realizada: ${cyan}$curl_request"
$curl_request > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json | jq
echo ""

## Respuesta incorrecta [404].
echo -e "${red}------------------------------------------------------------------------"
echo "Obtener detalles de una pelicula especifica. Respuesta incorrecta [404]."
echo -e "------------------------------------------------------------------------${NC}"
curl_request="curl -s "$localhost/peliculas/100000""
echo -e "Consulta realizada: ${cyan}$curl_request"
$curl_request > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json | jq
echo ""

# Obtener una pelicula por genero:
## Respuesta correcta [200].
echo -e "${green}-------------------------------------------------------"
echo "Obtener peliculas por genero. Respuesta correcta [200]."
echo -e "-------------------------------------------------------${NC}"
curl_request="curl -s "$localhost/peliculas/genero/ciencia_ficcion""
echo -e "Consulta realizada: ${cyan}$curl_request"
$curl_request > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json | jq
echo ""

## Respuesta incorrecta [400].
echo -e "${red}---------------------------------------------------------"
echo "Obtener peliculas por genero. Respuesta incorrecta [400]."
echo -e "---------------------------------------------------------${NC}"
curl_request="curl -s "$localhost/peliculas/genero/232321""
echo -e "Consulta realizada: ${cyan}$curl_request"
$curl_request > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json | jq
echo ""

# Obtener peliculas por titulo
## Respuesta correcta [200].
echo -e "${green}-------------------------------------------------------"
echo "Obtener peliculas por titulo. Respuesta correcta [200]."
echo -e "-------------------------------------------------------${NC}"
curl_request="curl -s "$localhost/peliculas/buscar/the_lord_of_the_rings""
echo -e "Consulta realizada: ${cyan}$curl_request"
$curl_request > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json | jq
echo ""

## Respuesta incorrecta [400].
echo -e "${red}---------------------------------------------------------"
echo "Obtener peliculas por titulo. Respuesta incorrecta [400]."
echo -e "---------------------------------------------------------${NC}"
curl_request="curl -s "$localhost/peliculas/buscar/232321""
echo -e "Consulta realizada: ${cyan}$curl_request"
$curl_request > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json | jq
echo ""


# Obtener una pelicula random sugerida
## Respuesta correcta [200].
echo -e "${green}---------------------------------------------------------------"
echo "Obtener una pelicula random sugerida. Respuesta correcta [200]."
echo -e "---------------------------------------------------------------${NC}"
curl_request="curl -s "$localhost/peliculas/sugerir""
echo -e "Consulta realizada: ${cyan}$curl_request"
$curl_request > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json | jq
echo ""


# Obtener una pelicula random sugerida por genero
## Respuesta correcta [200].
echo -e "${green}--------------------------------------------------------------------------"
echo "Obtener una pelicula random sugerida por genero. Respuesta correcta [200]."
echo -e "--------------------------------------------------------------------------${NC}"
curl_request="curl -s "$localhost/peliculas/sugerir/ciencia_ficcion""
echo -e "Consulta realizada: ${cyan}$curl_request"
$curl_request > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json | jq
echo ""

## Respuesta incorrecta [400].
echo -e "${red}----------------------------------------------------------------------------"
echo "Obtener una pelicula random sugerida por genero. Respuesta incorrecta [400]."
echo -e "----------------------------------------------------------------------------${NC}"
curl_request="curl -s "$localhost/peliculas/sugerir/232321""
echo -e "Consulta realizada: ${cyan}$curl_request"
$curl_request > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json | jq
echo ""


# Obtener una pelicula random sugerida por genero indicando el proximo feriado
## Respuesta correcta [200].
echo -e "${green}---------------------------------------------------"
echo "Pelicula al azar por el genero indicando mostrando"
echo "el próximo feriado. Respuesta correcta [200]."
echo -e "---------------------------------------------------${NC}"
curl_request="curl -s "$localhost/peliculas/recomendacion/drama""
echo -e "Consulta realizada: ${cyan}$curl_request"
$curl_request > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json | jq 
echo ""

echo -e "${blue}=================================="
echo "Fin de las pruebas del metodo GET."
echo "=================================="
echo ""
echo ""


# Inicio de pruebas del metodo POST:
echo -e "${yellow}=================================="
echo "Inicio de pruebas del metodo POST."
echo "=================================="
echo ""

# Crear una nueva pelicula:
## Respuesta correcta [201].
echo -e "${green}---------------------------------------------------"
echo "Crear una nueva pelicula. Respuesta correcta [201]."
echo -e "---------------------------------------------------${NC}"
data='{"titulo": "The Super Mario Bros.", "genero": "Infantil"}' # Datos de la pelicula en JSON
curl_command="curl -s -X POST -H \"Content-Type: application/json\" -d \"$data\" \"$localhost/peliculas\""
curl_request=$(curl -s -X POST -H "Content-Type: application/json" -d "$data" "$localhost/peliculas")
echo -e "Consulta realizada: ${cyan}$curl_command"
echo "$curl_request" > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json | jq
echo ""

## Respuesta incorrecta [400].
echo -e "${red}-----------------------------------------------------"
echo "Crear una nueva pelicula. Respuesta incorrecta [400]."
echo -e "-----------------------------------------------------${NC}"
data='{"titulo": "", "genero": "Fantasía"}' # Datos de la pelicula en JSON
curl_command="curl -s -X POST -H \"Content-Type: application/json\" -d \"$data\" \"$localhost/peliculas\""
curl_request=$(curl -s -X POST -H "Content-Type: application/json" -d "$data" "$localhost/peliculas")
echo -e "Consulta realizada: ${cyan}$curl_command"
echo "$curl_request" > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json | jq
echo ""

echo -e "${blue}==================================="
echo "Fin de las pruebas del metodo POST."
echo "==================================="
echo ""
echo ""


# Inicio de pruebas del metodo PUT:
echo -e "${yellow}================================="
echo "Inicio de pruebas del metodo PUT."
echo "================================="
echo ""

# Actualizar una pelicula:
## Respuesta correcta [200].
echo -e "${green}--------------------------------------------------"
echo "Actualizar una pelicula. Respuesta correcta [200]."
echo -e "--------------------------------------------------${NC}"
data='{"id": "13", "titulo": "Avatar", "genero": "Aventura"}' # Datos de la pelicula en JSON
curl_command="curl -s -X PUT -H \"Content-Type: application/json\" -d \"$data\" \"$localhost/peliculas/9\""
curl_request=$(curl -s -X PUT -H "Content-Type: application/json" -d "$data" "$localhost/peliculas/9")
echo -e "Consulta realizada: ${cyan}$curl_command"
echo "$curl_request" > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json | jq
echo ""

## Respuesta incorrecta [400].
echo -e "${red}----------------------------------------------------"
echo "Actualizar una pelicula. Respuesta incorrecta [400]."
echo -e "----------------------------------------------------${NC}"
data='{"id": "13", "titulo": "", "genero": "Aventura"}' # Datos de la pelicula en JSON
curl_command="curl -s -X PUT -H \"Content-Type: application/json\" -d \"$data\" \"$localhost/peliculas/9\""
curl_request=$(curl -s -X PUT -H "Content-Type: application/json" -d "$data" "$localhost/peliculas/9")
echo -e "Consulta realizada: ${cyan}$curl_command"
echo "$curl_request" > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json | jq
echo ""

## Respuesta incorrecta [404].
echo -e "${red}----------------------------------------------------"
echo "Actualizar una pelicula. Respuesta incorrecta [404]."
echo -e "----------------------------------------------------${NC}"
data='{"id": "132938129371", "titulo": "Avatar", "genero": "Aventura"}' # Datos de la pelicula en JSON
curl_command="curl -s -X PUT -H \"Content-Type: application/json\" -d \"$data\" \"$localhost/peliculas/100000\""
curl_request=$(curl -s -X PUT -H "Content-Type: application/json" -d "$data" "$localhost/peliculas/100000")
echo -e "Consulta realizada: ${cyan}$curl_command"
echo "$curl_request" > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json | jq
echo ""

echo -e "${blue}=================================="
echo "Fin de las pruebas del metodo PUT."
echo "=================================="
echo ""
echo ""

# Inicio de pruebas del metodo DELETE:
echo -e "${yellow}====================================="
echo "Inicio de pruebas del metodo DELETE."
echo "====================================="
echo ""

# Eliminar una pelicula:
## Respuesta correcta [200].
echo -e "${green}------------------------------------------------"
echo "Eliminar una pelicula. Respuesta correcta [200]."
echo -e "------------------------------------------------${NC}"
curl_command="curl -s -X DELETE \"$localhost/peliculas/50\""
curl_request=$(curl -s -X DELETE "$localhost/peliculas/50")
echo -e "Consulta realizada: ${cyan}$curl_command"
echo "$curl_request" > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json | jq
echo ""

## Respuesta incorrecta [404].
echo -e "${red}--------------------------------------------------"
echo "Eliminar una pelicula. Respuesta incorrecta [404]."
echo -e "--------------------------------------------------${NC}"
curl_command="curl -s -X DELETE \"$localhost/peliculas/100000\""
curl_request=$(curl -s -X DELETE "$localhost/peliculas/100000")
echo -e "Consulta realizada: ${cyan}$curl_command"
echo "$curl_request" > resultado.json
echo -e "${NC}El resultado es: "
cat resultado.json | jq
echo ""

echo -e "${blue}====================================="
echo "Fin de las pruebas del metodo DELETE."
echo "====================================="
echo ""