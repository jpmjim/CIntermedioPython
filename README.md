# Curso de Python: Comprehensions, Lambdas y Manejo de Errores

El Zen de Python
----------------
Son los 20 principios de software más importantes que tiene este lenguaje de progrmación para escribir lineas de codigo de manera correcta y precisa.
  - Para verlo ingresamos a la terminal dentro de python "import this" modulo oculto donde se encuentran los 20 principios.


Entorno virtual
---------------
Los entornos virtuales son de mucha utilidad ya que nos ayudan a tener versiones especificas de librerías o módulos a un proyecto sin afectar a otros. De esta forma en el mismo equipo pueden coexistir distintos proyectos con distintas versiones de la misma librería o modulo.

Creación del ambiente virtual
 - Dentro de una carpeta con el nombre del proyecto "vproyecto"
 - Inicializamos como un repositorio git con "git init"
 - Ejecutamos "python -m venv nombre_venv" usualmente el nombre venv es utilizada comunidad de python
 - Comando para activar el entorno virtual "source venv/bin/activate"
 - Desactivar el ambiente con "deactivate".
 - Crear un alias es "alias nombre_alias='_comando_'"

Instalación de dependencias con pip
-----------------------------------

Módulos populares dentro de python son:
  - Requests
  - BeautifulSoup4
  - Pandas
  - Numpy
  - Pytest

comandos:
  - pip freeze -> nos muestra que modulos tenemos instalados.
  - pip install pandas -> instalación del modulo pandas
  - Tener un archivos donde se encuentran la lista dependencias con sus versiones lo hacemos con "pip freeze > requirements.txt", para compartirlo.
  - Para instalar la lista usamos "pip install -r requirements.txt".

Una alternativa que podemos usar "ANACONDA" principalmente usada en ciencia de datos, tambien para creación de entorno vitual y instalar dependencias de manera gráfica.No recomendable para backend. https://www.anaconda.com/products/individual


- Básicamente, pip es como el npm de JavaScript, y el archivo requeriments.txt es como el package. json de JavaScript.

- Es importante recordar que esto se debe correr con el entorno virtual activado (avenv), de esta manera todas las dependencias que instalemos se guardaran para este entorno virtual (de lo contrario se guardarían de manera global, que es justo lo que no queremos).

- Algo importante, si estás manejando git, es bueno siempre ignorar la carpeta venv, esto porque realmente no nos importa subir todo eso al repositorio, puedes mirarlo como que venv es el node_modules de JavaScript, a fin de cuentas, cualquier otro programador que trabaje con nuestro código creará su propio entorno virtual e instalará las dependencias que dejamos en nuestro requeriments.txt.

- Y un dato curioso es que, el operador > en la terminal es algo especial de UNIX, ya que este operador lo que hace es redirigir la salida de cualquier comando hacia donde lo mandes, por defecto la salida es en la terminal, pero al usar > le dijimos a la terminal que, en lugar de que la salida sea en la terminal, que se redirija al archivo requeriments.txt 👀. Si quieren jugar con ello, pueden hacerlo con este ejemplo: ls -al > test.txt, eso creará un archivo llamado test.txt, y si lo abren verán cómo es que ese comando funciona 

Funciones anónimas: lambda
--------------------------
Son funciones que no tienes un identificador sin nombre, estructurado de esta manera "lambda argumentos: expresión" pueden contener los arguemntos que necesitemos pero solo una linea de código una sola expresión. Lambda ya no es necesario te colocar el return.
Ejmplo: 
Uso de lambda
    "identificador"    "argumento"   "expresión"
       palindrome   =  lambda string: string == string[::-1]   
       print(palindrome('ana'))
       Nos devuelve "True"
      
Función normal
    def palindrome(string):
        return string == string[::*1]
    print(palindrome('ana'))

Pequeñas funciones anónimas pueden ser creadas con la palabra reservada "lambda"

High order functions "Funciones de orden superior"
--------------------
Es una función que recibe como parametro a otra funcion.Tiene tres funciones de orden superior que son filter, man y reduce.

![alt text](https://miro.medium.com/max/1200/1*DreeF8a4h2pvxRly39HjAA.jpeg)


Filter
Devuelve True or False según el valor esté dentro de los criterios buscados o no. En caso de que no cumpla con la condición, no será devuelto y la lista se verá reducida por este filtro.
 my_list = [1,4,5,6,9,13,19,21]
 odd = list(filter(lambda x: x%2 !=0, my_list))
 print(odd)

Map
Funciona muy parecido, pero su diferencia radica en que no puede eliminar valores de la lista del array entregado. Es decir, el output tiene la misma cantidad de valores que el input.
 my_list = [1,2,3,4,5]
 squares = list(map(lambda x: x**2, my_list))
 print(squares)

Reduce
Tenemos que importar esta función desde functools para poder usarla, tiene los mismos argumentos que las anteriores funciones, reduce el iterable por medio de la función anonima.
La función de reducción necesita de dos parámetros, uno que almacena el resultado (o el primer valor del iterable) y otro que opera con el siguiente valor del iterable.
 from functools import reduce
 my_list = [2,2,2,2,2]
 all_multiplied= reduce(lambda a, b: a * b, my_list)
 print(all_multiplied)


Los errores en el código
------------------------
El manejo de errores es muy importante y los mejores trucos son:
 - Leer el error (Conozco programadores y hasta yo en un inicio trataba de revisar el código sin revisar el traceback)
 - Leer el traceback de abajo hacia arriba
 - Errores de Sintaxis (SyntaxError) → escribimos mal alguna palabra clave (typo), el programa no se ejecuta.
 - Excepciones (Exeption) → Producen un colapso o interrupción de la lógica del programa en alguna línea en específico por ejemplo (todas las líneas anteriores se ejecutan), pueden ser de varios tipos, generalmente aparecen cuando no existe un componente clave en la ejecución o hay alguna imposibilidad lógica (matemática) para efectuar la instrucción, tambipen pueden generarse dentro del código o fuera de el (elevar una excepción)

Elevar una excepción:
 - Cuando tenemos una excepción en python lo que sucede es que se crea un objeto de tipo exception que se va moviendo a través de los bloques de código hasta llegar al bloque principal si es que no se maneja dicha excepción en algún bloque intermedio el programa se interrumpe y genera el traceback


Lectura de un traceback:
 - La manera correcta de leer un traceback es iniciar por el final, en el caso de un error de sintaxis nos indicará en qué línea se encuentra dicho error.
 - En el caso de excepciones la última línea nos indicará el tipo de exepcion que se generó (generalmente son autoexplicativas pero si no entienedes que paso puedes buscar este error)
 - La penúltima línea nos indicará dende se encuentra el error (archivo y línea)
 - La antepenúltima línea nos muestra “most recent call last” lo que significa que la llamada más reciente es la última (el programa se cerró después de esa llamada, se genero un error)

Debugging
---------
O depuración es una herramienta que traen varios editores de código con el objetivo de solucionar nuestros errores de lógica. Revisemos la herramienta debugging de VSCode.

En este entorno podemos acceder a funcionalidades como:
 - pause → permite pausar la ejecución del programa
 - step over → permite avanazr un solo paso en el programa
 - step in → igresamos a un bloque secundario del programa (funciones)
 - step out → salimos del bloque secundario
 - restart → reinicia el programa
 - stop → detiene el programa

Además podemos generar breakpoints, que son puntos en los que el programa se detendrá para ayudarnos a depurar el código

Nota:
    Existen herramientas de debugging propias de python como el módulo pdb o los breakpoints (a partir de python 3.7)

Manejo de excepciones
---------------------
Algo que aparece casi al final de la lectura recomendada en el documentación de Python es que se puede agregar un “else” al try-except.

- TRY: En el try se coloca código que esperamos que pueda lanzar algún error.
- EXCEPT: En el except se maneja el error, es decir, si ocurre un error dentro del bloque de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.
- FINALLY: Se ejecuta SIEMPRE, haya sido lanzada la excepción o no haya sido lanzada.

![alt text](https://static.platzi.com/media/user_upload/python-a0d427c5-4e5b-49cd-8e69-3e3b118f37ce.jpg)