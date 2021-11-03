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


Básicamente, pip es como el npm de JavaScript, y el archivo requeriments.txt es como el package.json de JavaScript.
.
Es importante recordar que esto se debe correr con el entorno virtual activado (avenv), de esta manera todas las dependencias que instalemos se guardaran para este entorno virtual (de lo contrario se guardarían de manera global, que es justo lo que no queremos).
.
Algo importante, si estás manejando git, es bueno siempre ignorar la carpeta venv, esto porque realmente no nos importa subir todo eso al repositorio, puedes mirarlo como que venv es el node_modules de JavaScript, a fin de cuentas, cualquier otro programador que trabaje con nuestro código creará su propio entorno virtual e instalará las dependencias que dejamos en nuestro requeriments.txt.
.
Y un dato curioso es que, el operador > en la terminal es algo especial de UNIX, ya que este operador lo que hace es redirigir la salida de cualquier comando hacia donde lo mandes, por defecto la salida es en la terminal, pero al usar > le dijimos a la terminal que, en lugar de que la salida sea en la terminal, que se redirija al archivo requeriments.txt 👀. Si quieren jugar con ello, pueden hacerlo con este ejemplo: ls -al > test.txt, eso creará un archivo llamado test.txt, y si lo abren verán cómo es que ese comando funciona 