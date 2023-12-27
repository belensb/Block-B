<div align="center">

<h1 style="border-bottom: none">
    <b><a href="#">BLOCK-B</a></b>
</h1>

Aplicación web diseñada por el grupo 6 de la comisión 7 del `Informatorio`<br>
Consiste en un blog para la divulgación de información referida a libros.

![GitHub repo size](https://img.shields.io/github/repo-size/SBelenB/Proyecto_Final)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

</div>

## Comenzando 🚀

Para obtener una copia del proyecto funcionando en tu PC de manera local para propósitos de desarrollo y pruebas, seguí las instrucciones

> [!NOTE]  
> Si preferís no clonar el proyecto en tu computadora local, podés verlo directamente <b><a href="https://grupo6info.pythonanywhere.com/">_aquí_</a></b>.

### Pre-requisitos 📋

Antes de iniciar, es recomendable generar un entorno virtual de trabajo donde instalaremos las dependencias necesarias para que el proyecto funcione. Para ello, abrimos el CMD y nos dirigimos a la carpeta donde queremos guardar el entorno virtual y ejecutamos el siguiente comando:


```
python3 -m venv nombre_del_entorno

```
Una vez creado es necesario activarlo para ello ejecutamos la siguiente linea (en Windows):


```
nombre_del_entorno\Scripts\activate.bat

```

Ya contamos con un entorno virtual activado en el cual podemos instalar todas las dependencias para correr nuestro proyecto.


Luego, con el entorno activado, no dirigimos a la carpeta donde se encuentra el archivo requirements.txt y ejecuta el siguiente comando en la consola.

```
pip install -r requirements.txt

```
Este comando instalará en nuestro entorno, todo lo necesario para que el proyecto funcione funciona correctamente.

### SETTINGS 🔧

Luego tenes que crear un archivo de configuraciones en la carpeta fundacion_pueblo/settings/ y llamala "local.py", donde debes indicar las credenciales de tu base de datos como se muestra a continuacion.

```
from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'databaseName',
        'USER': 'databaseUser',
        'PASSWORD': 'databasePassword',
        'HOST': 'localhost',
        'PORT': 'portNumber',
    }
}

```


## Construido con 🛠️

Las herramientas utilizadas para el desarrollo fueron:

* [Django](https://www.djangoproject.com/) Framework web
* [Python](https://www.python.org/) Del lado del servidor (backend)
* [Bootstrap](https://getbootstrap.com/) Framework web para el desarrollo frontend (HTML, CSS, JavaScript)
* [MySql](https://www.mysql.com/) - Sistema de gestión de bases de datos.


## Autores ✒️

Este proyecto fue desarrollado gracias a la colaboración de:

* **Tomas Martinez** - Docente - Desarrollo WEB y Bases de Datos.

* **Maximiliano mauro Blanco**<br>
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mangadetransas)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/maxi-blanco-59a523245/)
  
* **Rocio Belén Gimenez**<br>
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/SBelenB)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/belengimenez/)
  
* **Héctor Ezequiel  Morales**<br>
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/elezejab)


También puedes mirar la lista de todos los [contribuyentes](https://github.com/tomimartinez28/blog-comision-7/graphs/contributors) quíenes han participado en este proyecto. 




---
