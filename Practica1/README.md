BIENVENIDO!
A continuacion encontraras todo lo que necesitas saber para el uso de SimpleQL.

Para comenzar, debes saber que SimpleQL está hecho con el fin de manejar de forma
rapida y sencilla la informacion de archivos con extension .json, debes tener en
cuenta que no se podra leer ningun otro tipo de archivo, ademas, tus archivos
deberan cumplir con tener solo los parametros: nombre, edad, activo y promedio.

Antes de utilizar SimpleQL debes tener la version 3.8.5 de python para que
SimpleQL pueda funcionar de la mejor forma.

Recuerda que SimpleQL es una herramienta que se utiliza en modo consola asi que
tendras que aprender los comandos existentes en SimpleQL y presionar ENTER para 
hacer que funcionen. No te preocupes, a continuacion encontrarar cada comando 
con su funcion y su forma de uso.

Ahora si, comencemos!

============================ Carga de Datos ==================================

Para utilizar tus datos en SimpleQl, primero tienes que cargarlos, para ello
utilizaremos el comando CARGAR, seguido por la direccion de tu archivo.
Recuerda, SimpleQL es capaz de leer mas de un archivo a la vez, para ello debes
colocar la ruta de cada uno de los archivos, separados por una coma, y no
olvides colocar un espacio luego de cada una.

*NOTA: si tus archivos estan dentro de la misma carpeta que el programa, basta
con colocar el nombre junto con su extension.

Ejemplo:

    CARGAR archivo1.json, archivo2.json

========================= Visualizacion de Datos =============================

Para poder visualizar cada registro utilizaremos el comando SELECT, este tendra
las siguientes variantes:

1) Si quieres mostrar todos los registros con cada uno de sus datos deberas
escribir un ASTERISCO despues del comando

Ejemplo:

    SELECT *

2) Podemos solicitar campos especificos de los registros, para ello, luego de
el comando SELECT escribiremos el nombre de los campos separados por comas.

Ejemplo:

    Select nombre, edad

    Esto nos mostraria el nombre y edad de cada registro.

3) Podemos mostrar todos los registros que cumplan con alguna condicion, esto
con el fin de poder hacer busquedas. para ello añadiremos un comando extra
llamado DONDE. Y luego colocaremos la condicion.

*NOTA: para los campos que guardan texto como el nombre, la condicion debera
escribirse entre comillas dobles ""

Ejemplo:

    SELECT * DONDE nombre = "nombreDePrueba"

Recuerda que solamente podras utilizar una condicion de busqueda.

4) Podemos mostrar solamente algunos campos de los registros que cumplan una
condicion mezclando el caso 3 y el caso 2.

Ejemplo:

    SELECT nombre DONDE edad = 50

==================================== Suma ====================================

La funcion SUMA se encargara de sumar todas las cantidades de un campo a
nuestra eleccion. (solo puede ser EDAD o PROMEDIO)

Ejemplo:

    SUMA edad

=================================== Cuenta ===================================

El comando cuenta nos devolvera la cantidad de registros que hemos cargado en
SimpleQL

Ejemplo:

    CUENTA

=================================== Maximo ===================================

Este comando nos mostrara el valor mas alto entre todos los registros de un 
campo a nuestra eleccion. (solamente puede ser edad ó promedio)

Ejemplo:

    MAXIMO promedio

=================================== Minimo ===================================

Este comando nos mostrara el valor mas bajo entre todos los registros de un 
campo a nuestra eleccion. (solamente puede ser edad ó promedio)

Ejemplo:

    MINIMO edad

================================== Reportar ==================================

La ultima funcion de SimpleQL nos generara un reporte de los registros que
cargamos en SimpleQL, esto con el fin de que usted pueda acceder a su informa-
cion de forma mas ordenada y entendible. Para esto tendremos 2 variantes:

1) Reportar toda la informacion, para esto nos bastara el escribir el comando
REPORTAR.

Ejemplo:

    REPORTAR

2) Reportar solamente algunos de los registros, debe tomar en cuenta que usted
podra elegir la cantidad, pero no cuales seran los que se reporten, asi que el
programa generara un reporte de los primeros registros hasta llegar al numero
que usted solicite. Si ingresa un numero mayor a la cantidad de registros
existentes, el reporte sera de todos los registros. Para esto solamente debe
ingresar el comando, seguido de la cantidad de registros que desea.

Ejemplo:

    REPORTAR 3
    
*NOTA: El reporte se generara en un archivo llamado REPORTE.html, el cual
se abrira en tu navegador pre-determinado al momento de usar el comando.

=========================== Cosas a considerar ===============================

Los archivos REPORTE.html y auxiliar.json son necesarios para el funcionamien-
to de SimpleQL. Si en algun momento eliminas uno de estos, basta con crear
nuevamente los archivos con el mismo nombre y extension.

================================== FIN =======================================

GRACIAS POR USAR SimpleQL! ESPERAMOS QUE TENGAS UNA GRATA EXPERIENCIA!