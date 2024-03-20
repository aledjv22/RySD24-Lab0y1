#!/usr/bin/env python
# encoding: utf-8
"""
hget: un cliente HTTPS simple

Escrito con fines didacticos por la catedra de
Redes y Sistemas Distribuidos,
FaMAF-UNC

El proposito de este codigo es mostrar con un ejemplo concreto las primitivas
basicas de comunicacion por sockets; no es para uso en produccion (para eso
esta el modulo urllib de la biblioteca estandar de python que contiene un
cliente HTTP mucho mas completo y correcto.
Revision 2019 (a Python 3): Pablo Ventura
Revision 2011: Eduardo Sanchez
Original 2009-2010: Natalia Bidart, Daniel Moisset

"""

import sys
import socket
import ssl
import optparse

PREFIX = "https://"
HTTPS_PORT = 443   # El puerto por convencion para HTTPS,
# según http://tools.ietf.org/html/rfc1700
HTTPS_OK = "200"  # El codigo esperado para respuesta exitosa.


def parse_server(url):
    """
    Obtiene el server de una URL. Por ejemplo, si recibe como input
    "https://www.famaf.unc.edu.ar/carreras/computacion/computacion.html"
    devuelve "www.famaf.unc.edu.ar"

    El llamador es el dueño de la memoria devuelta

    Precondicion: url es un str, comienza con PREFIX
    Postcondicion:
        resultado != NULL
        url comienza con PREFIX + resultado
        '/' not in resultado
        resultado es la cadena mas larga posible que cumple lo anterior

    >>> parse_server('https://docs.python.org/library/intro.html')
    'docs.python.org'

    >>> parse_server('https://google.com')
    'google.com'

    >>> parse_server('google.com') # Falta el prefijo, deberia fallar
    Traceback (most recent call last):
       ...
    AssertionError

    """
    assert url.startswith(PREFIX)
    # Removemos el prefijo:
    path = url[len(PREFIX):]
    path_elements = path.split('/')
    result = path_elements[0]

    assert url.startswith(PREFIX + result)
    assert '/' not in result

    return result


def connect_to_server(server_name):
    """
    Se conecta al servidor llamado server_name

    Devuelve el socket conectado en caso de exito, o falla con una excepcion
    de socket.connect / socket.gethostbyname.

    >>> type(connect_to_server('www.famaf.unc.edu.ar')) # doctest: +ELLIPSIS
    <class 'socket.socket'>

    >>> connect_to_server('no.exis.te') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
       ...
    gaierror: [Errno -5] No address associated with hostname
HTTP_REQUEST = b"GET %s HTTP/1.1\r\n\r\n"
    >>> connect_to_server('localhost')
    Traceback (most recent call last):
       ...
    ConnectionRefusedError: [Errno 111] Connection refused
    """

    # Buscar direccion ip
    # COMPLETAR ABAJO DE ESTA 
    # Aqui deberian obtener la direccion ip del servidor y asignarla
    # a ip_address
    ip_address = socket.gethostbyname(server_name)
    # DEJAR LA LINEA SIGUIENTE TAL COMO ESTA
    sys.stderr.write("Contactando al servidor en %s...\n" % ip_address)
    # Crear socket

    # Un socket es una abstracción de comunicación que permite que diferentes 
    # procesos en una red intercambien datos. Básicamente, un socket es un punto 
    # final de una conexión bidireccional entre dos programas en una red. Permite 
    # que estos programas se comuniquen entre sí, ya sea en la misma máquina o en 
    # máquinas diferentes a través de una red.

    # COMPLETAR ABAJO DE ESTA LINEA
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip_address, HTTPS_PORT))
    # SSL Context creation
    context = ssl.create_default_context()
    sock = context.wrap_socket(sock, server_hostname = server_name)
    # Aqui deben conectarse al puerto correcto del servidor
    
    return sock
    # NO MODIFICAR POR FUERA DE ESTA FUNCION


def send_request(connection, url):
    """
    Envia por 'connection' un pedido HTTPS de la URL dada

    Precondicion:
        connection es valido y esta conectado
        url.startswith(PREFIX)
    """

    # Parse the URL manually
    schema = url.find('://')
    if schema != -1:
        url = url[schema + 3:]

    slash = url.find('/')
    if slash != -1:
        host = url[:slash]
        path = url[slash:]
    else:
        host = url
        path = '/'

    # Construct the HTTP request
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    connection.send(request.encode())
    
    

def read_line(connection):
    """
    Devuelve una linea leida desde 'connection`; hasta el siguiente '\n'
    (incluido), o hasta que se terminen los datos.

    Si se produce un error, genera una excepcion.
    """
    result = b''
    error = False
    # Leer de a un byte
    try:
        data = connection.recv(1)
    except:
        error = True
    while not error and data != b'' and data != b'\n':
        result = result + data
        try:
            data = connection.recv(1)
        except:
            error = True
    if error:
        raise Exceptiosend_requestn("Error leyendo de la conexion!")
    else:
        result += data  # Add last character
        return result


def check_https_response(header):
    """
    Verifica que el encabezado de la respuesta este bien formado e indique
    éxito. Un encabezado de respuesta HTTPS tiene la forma

    HTTPS/<version> <codigo> <mensaje>

    Donde version tipicamente es 1.0 o 1.1, el codigo para exito es 200,
    y el mensaje es opcional y libre pero suele ser una descripcion del
    codigo.url

    >>> check_https_response(b"HTTPS/2.0 200 Ok")
    True

    >>> check_https_response(b"HTTPS/2.0 200")
    True

    >>> check_http_response(b"HTTP/2.0 301 Permanent Redirect")
    False

    >>> check_http_response(b"Malformed")
    False
    """
    header = header.decode()
    elements = header.split(' ', 3)
    return (len(elements) >= 2 and elements[0].startswith("HTTP/")
            and elements[1] == HTTPS_OK)


def get_response(connection, filename):
    """
    Recibe de `connection' una respuesta HTTPS, y si es valida la descarga
    en un archivo llamdo `filename'.

    Devuelve True en caso de éxito, False en caso contrario
    """
    BUFFER_SIZE = 4096
    TIMEOUT = 5  # Timeout in seconds

    # Set the timeout
    connection.settimeout(TIMEOUT)

    # Verificar estado
    header = read_line(connection)
    if not check_https_response(header):
        sys.stdout.write("Encabezado HTTPS malformado: '%s'" % header.strip())
        return False
    else:
        # Saltear el resto del encabezado
        line = read_line(connection)
        while line != b'\r\n' and line != b'':
            line = read_line(connection)

        # Descargar los datos al archivo

        with open(filename, "wb") as output:
            while True:
                data = connection.recv(BUFFER_SIZE)
                if not data:
                    # No more data is available, exit the loop
                    break
                output.write(data)
                if b"</html>" in data:
                    # Exit the loop if "</html>" is found in the current chunk
                    break


    return True





def download(url, filename):
    """send_request
    Descarga por https datos desde `url` y los guarda en un nuevo archivo
    llamado `filename`
    """
    # Obtener server
    server = parse_server(url)
    sys.stderr.write("Contactando servidor '%s'...\n" % server)

    try:
        connection = connect_to_server(server)
    except socket.gaierror:
        sys.stderr.write("No se encontro la direccion '%s'\n" % server)
        sys.exit(1)
    except socket.error:
        sys.stderr.write("No se pudo conectar al servidor HTTPS en '%s:%d'\n"
                         % (server, HTTPS_PORT))
        sys.exit(1)

    # Enviar pedido, recibir respuesta
    try:
        sys.stderr.write("Enviando pedido...\n")
        send_request(connection, url)
        sys.stderr.write("Esperando respuesta...\n")
        result = get_response(connection, filename)
        if not result:
            sys.stderr.write("No se pudieron descargar los datos\n")
    except Exception as e:
        sys.stderr.write("Error al comunicarse con el servidor\n")
        # Descomentar la siguiente línea para debugging:
        # raise
        sys.exit(1)


def main():
    """Procesa los argumentos, y llama a download()"""
    # Parseo de argumentos
    parser = optparse.OptionParser(usage="usage: %prog [options] https://...")
    parser.add_option("-o", "--output", help="Archivo de salida",
                      default="download.html")
    options, args = parser.parse_args()
    if len(args) != 1:
        sys.stderr.write("No se indico una URL a descargar\n")
        parser.print_help()
        sys.exit(1)

    # Validar el argumento
    url = args[0]
    if not url.startswith(PREFIX):
        sys.stderr.write("La direccion '%s' no comienza con '%s'\n" % (url,
                                                                       PREFIX))
        sys.exit(1)

    download(url, options.output)


if __name__ == "__main__":
    main()
    sys.exit(0)
