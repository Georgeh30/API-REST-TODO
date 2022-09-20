# API-REST-TODO
REST API created with DJANGO API REST FRAMEWORK for the use of the TO DO web application where the only data is the task title and its description

## Creacion de archivo [.gitignore](https://www.toptal.com/developers/gitignore/)
### 1. Desde la pagina [toptal](https://www.toptal.com/developers/gitignore/?templates=django), crearemos el archivo especial para django, para ello podemos copiar o guardar como `.gitignore` en la carpeta raiz de este proyecto, si copiamos los datos, tendremos que ejecutar los comandos de abajo para crear el archivo y pegar estos datos en el y despues apretando (`CTRL + C`) para terminar el proceso
    copy con .gitignore

## Steps for the creation of [Django](https://docs.djangoproject.com/en/4.1/intro/tutorial01/) Project

### 1. Validar que se tenga instalado el entorno virtual [virtualenv](https://omes-va.com/virtualenv-python/), en caso de no tenerlo instalado ejecutar el segundo comando
    pip list o pip freeze
    pip install virtualenv
### 2. Verificamos que la terminal detecte el entorno vitual, mostrando la version instalada, en caso de marcar error al ejecutar el primer comando, desinstalaremos el modulo `virtualenv` y lo volvemos a instalar, para volver a validar que detecte el comando `virtualenv`.
    virtualenv --version
    pip uninstall virtualenv
    pip install virtualenv
### 3. Creacion del Entorno Virtual
    virtualenv virtual_environment_name
### 4. Activacion y Desactivacion del Entorno Virtual
    .\env\Scripts\activate
    .\env\Scripts\deactivate
### 5. Asegurando que esta activo el Entorno Virtual, Instalaremos el [Framework Django](https://docs.djangoproject.com/es/4.1/topics/install/#installing-official-release)
    py -m pip install Django
### 6. Verificamos que la terminal detecte el Framework Django, mostrando la version instalada, en caso de no detectar el modulo `django`, desinstalaremos el modulo y lo volvemos a instalar, para volver a validar la version del modulo.
    python -m django --version
    py -m pip uninstall Django
    py -m pip install Django
### 7. Creacion del nuevo proyecto [Django](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react), se recomienda llamarlo `config`
    django-admin startproject project's_name .
### 8. Creando la carpeta `core` e ingresando a ella para la creacion de la nueva aplicacion
    mkdir core
    cd core
    python ..\manage.py startapp app_name
### 9. Ingresamos al archivo `core/app_name/apps.py` y agregamos el nombre de la carpeta `core.` dentro de la variable name que esta dentro de la clase que se crea por default
    from django.apps import AppConfig

    class TodoConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'core.todo'
### 10. Creamos el archivo llamado `__init__` dentro de la carpeta `core` con el siguiente comando y en seguida apretando (`CTRL + C`) para terminar de crear el archivo, este archivo debera ser creado en el mismo nivel de las carpetas de las aplicaciones que se crean dentro de la carpeta `core`
    copy con __init__.py
### 11. Regresando a la carpeta raiz, ejecutar la `migrate` para crear la base de datos SQLite y crear las tablas que vienen por default en Django
    cd ..
    python manage.py migrate
### 12. Correr el Servidor y navegue a `http://localhost:8000` en el navegador, para detener el Servidor (`CTRL + C`), tambien se puede navegar en otro puerto ej: 3000
    python manage.py runserver
    python manage.py runserver 3000
### 13. Para obtener un listado de todos los comandos que se pueden ejecutar con `manage.py`
    python manage.py --help
### 14. Registro de la app `core.app_name` dentro del archivo `project's_name/settings.py`, dentro de la lista de la variable `INSTALLED_APPS`
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'core.app_name',
    ]
### 15. Creacion de `Mapeo Objeto-Relacional (ORM)` a través de `Clases` dentro del archivo `core/app_name/models.py`, en lugar de escribir consultas SQL, aunque podemos usar consultas SQL para los casos mas complejos
    from django.db import models

    # Create your models here.

    class Todo(models.Model):
        title = models.CharField(max_length=120)
        description = models.TextField()
        completed = models.BooleanField(default=False)

        def _str_(self):
            return self.title
### 16. Detenemos el servidor (`CTRL + C`) ya que al agregar, modificar o quitar codigo dentro del archivo `core/app_name/models.py` se deberá ejecutar los siguientes dos comandos para crear un archivo de migracion y para aplicarlos en la base de datos
    python manage.py makemigrations
    python manage.py migrate
### 17. Para probar el CRUD del `modelo (tabla)` creado, se deberá agregar este `modelo` en el archivo `core/app_name/admin.py`
    from django.contrib import admin
    from .models import Todo

    class TodoAdmin(admin.ModelAdmin):
        list_display = ('title', 'description', 'completed')

    # Register your models here.

    admin.site.register(Todo, TodoAdmin)
### 18. Creación de la cuenta `superuser` para acceder a la interfaz de administración
    python manage.py createsuperuser

    Username (leave blank to use 'Computer_UserName'): superuser_name
    Email address: personal_email
    Password: password_we_want_to_use
    Password (again): confirm_password
    Superuser created successfully.
### 19. Volvemos a correr el servidor e ingresamos a la ruta `http://localhost:8000/admin`, deberemos iniciar sesion como `superuser` con el nombre y contraseña que asignamos, para poder ingrezar a la interfaz y realizar el CRUD (crear, leer, actualizar, borrar)
    python manage.py runserver
### 20. Detenemos el servidor (`CTRL + C`) para poder configurar la [DJANGO REST FRAMEWORK](https://www.django-rest-framework.org/#installation) instalando `djangorestframework` y `django-cors-headers`, el ultimo nos sirve para poder evitar errores debidos a las reglas CORS y acortar la url
    py -m pip install djangorestframework django-cors-headers


### [Creacion](https://www.youtube.com/watch?v=90YKt9PlWZY) de archivo requirements.txt e [Instalacion](https://gist.github.com/kamikaze-lab/7d5987ff86223e1bf686) de estas dependencias
### 1. Para crear el archivo que especifica las dependencias requeridas para usar este proyecto y para la instalacion de las dependencias
    pip freeze > requirements.txt
    pip install -r requirements.txt

