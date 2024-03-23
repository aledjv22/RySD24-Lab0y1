
Opcionalmente, y con la posibilidad de que se otorguen puntos extras en la evaluación parcial, se pide investigar qué mecanismos permiten funcionar a nombres de dominio como:

- http://中文.tw/
- https://💩.la

Ayuda: investigue sobre el término “encoding”.

### Respuesta:
Para que se pueda utilizar [Unicode](https://en.wikipedia.org/wiki/Unicode) (el cual entre varias cosas se utiliza para otorgar soporte a distintos lenguajes e incluir emojis [3]) en el nombre de dominio de forma correcta es necesario hacer un encoding (codificacion de caracteres)  permite convertir un en este caso caracteres de un formato a otro. 
#### Por que es asi?
> En el caso del registro de nombres de dominio, un nombre de dominio puede contener únicamente los caracteres a-z, 0-9 y - (guion). No puede especificar un guion al principio o al final de una etiqueta.
> Amazon [5]

Esto limitaba considerablemente la posibilidad de utilizar caracteres de otros idiomas, emojis o símbolos especiales.
Para superar esta limitación, se introdujo el concepto de "encoding" o codificación de caracteres. El encoding permite convertir un conjunto de caracteres de un formato a otro, de manera que puedan ser interpretados por diferentes sistemas.
#### Nombre de dominio internacionalizado (IDN) [4]
Es un tipo de nombre de dominio de Internet que permite el uso de caracteres no ASCII, como letras acentuadas, caracteres de idiomas no latinos, y símbolos especiales de diversos idiomas. Para que estos caracteres no ASCII sean compatibles con el sistema de nombres de dominio (DNS), se utilizan técnicas de encoding como Punycode, que convierte estos caracteres en una forma que pueda ser interpretada por el DNS.

#### Punycode [1]
La representación ASCII comienza con el prefijo "xn--" y es seguida por el nombre de dominio que contiene caracteres unicode codificado como Punycode.
Por ejemplo [2]:
https://💩.la se codifica como https://xn--ls8h.la
 http://中文.tw/ se codifica como http://xn--fiq228c.tw

[1]: https://es.wikipedia.org/wiki/Punycode
[2]: https://dnschecker.org/idn-punycode-converter.php 
[3]: https://en.wikipedia.org/wiki/Emoji_domain
[4]: https://es.wikipedia.org/wiki/Nombre_de_dominio_internacionalizado
[5]: https://docs.aws.amazon.com/es_es/Route53/latest/DeveloperGuide/DomainNameFormat.html#domain-name-format-registration
