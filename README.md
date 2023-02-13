<a name="top"></a>

# API-REST-TODO
REST API created with DJANGO API REST FRAMEWORK for the use of the TO DO web application where the only data is the task title and its description

## Índice de contenidos
* [Correr Projecto en otras computadoras](#run_project_others_pc)
* [Instalacion del lenguaje python](#install_python)
* [Creacion de archivo .gitignore](#create_gitignore)
* [Steps for the creation of Django](#creation_django)
* [Install and config Django Rest Framework](#config_drf)
* [Creacion de Archivo requirements](#creation_requirements)


[Subir](#top)
<a name="run_project_others_pc"></a>

## Correr Projecto en otras computadoras

### 1. Se deberá tener [instalado](#intalacion_python) el lenguaje de programacion python
### 2. Una vez que se reconoce el comando `python` se deberá instalar el [entorno virtual](#entorno_virtual), [crear](#crear_venv) un nuevo entorno virtual, [activar](#activar_venv) el entorno virtual, [instalacion](#dependencias) de todas las demas dependencias y [corremos](#run_server) el servidor


## Creacion de archivo [.gitignore](https://www.toptal.com/developers/gitignore/)

### 1. Desde la pagina [toptal](https://www.toptal.com/developers/gitignore/?templates=django), crearemos el archivo especial para django, para ello podemos copiar o guardar como `.gitignore` en la carpeta raiz de este proyecto, si copiamos los datos, tendremos que ejecutar los comandos de abajo para crear el archivo y pegar estos datos en el y despues apretando (`CTRL + C`) para terminar el proceso
    copy con .gitignore

[Subir](#top)
<a name="install_python"></a>
<a name="intalacion_python"></a>

## Instalacion del lenguaje [python](https://www.youtube.com/watch?v=JqUV25aFRV0)

### 1. Descargamos del [Instalador](https://www.python.org/downloads/)
### 2. Abrimos el Instalador, marcamos la casilla `Add Python 3.10 to PATH` y seleccionamos `Install Now`
### 3. Seleccionamos `Disable path length limit` para terminar la instalacion damos click en el boton `close`
### 4. Verificamos en la consola (CMD) que reconozca el comando `python`
    python --version
    pip --version
### 5. En caso de no reconocer el comando `python`, deberemos agregarlo a las [variables de entorno](https://www.sintaxisweb.com/2019/03/adicione-python-la-variable-path-del.html#:~:text=En%20su%20equipo%20ubique%20la,el%20listado%20variable%20de%20entorno.)
### 6. Una vez que se reconoce el comando `python` se deberá instalar el [entorno virtual](#entorno_virtual), [activar](#activar_venv) el entorno virtual, [{instalar](#creation_django) el framework django e [instalacion](#dependencias) de todas las dependencias.


[Subir](#top)
<a name="create_gitignore"></a>

## Creacion de archivo [.gitignore](https://www.toptal.com/developers/gitignore/)

### 1. Desde la pagina [toptal](https://www.toptal.com/developers/gitignore/?templates=django), crearemos el archivo especial para django, para ello podemos copiar o guardar como `.gitignore` en la carpeta raiz de este proyecto, si copiamos los datos, tendremos que ejecutar los comandos de abajo para crear el archivo y pegar estos datos en el y despues apretando (`CTRL + C`) para terminar el proceso
    copy con .gitignore


[Subir](#top)
<a name="creation_django"></a>

## Steps for the creation of [Django](https://docs.djangoproject.com/en/4.1/intro/tutorial01/) Project

<a name="entorno_virtual"></a>

### 1. Validar que se tenga instalado el entorno virtual [virtualenv](https://omes-va.com/virtualenv-python/), en caso de no tenerlo instalado ejecutar el segundo comando
    pip list o pip freeze
    pip install virtualenv
### 2. Verificamos que la terminal detecte el entorno vitual, mostrando la version instalada, en caso de marcar error al ejecutar el primer comando, desinstalaremos el modulo `virtualenv` y lo volvemos a instalar, para volver a validar que detecte el comando `virtualenv`.
    virtualenv --version
    pip uninstall virtualenv
    pip install virtualenv

<a name="crear_venv"></a>

### 3. Creacion del Entorno Virtual
    virtualenv virtual_environment_name

<a name="activar_venv"></a>

### 4. Activacion y Desactivacion del Entorno Virtual
    .\env\Scripts\activate
    .\env\Scripts\deactivate

<a name="intalacion_django"></a>

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
### 11. Ahora ingresamos a la carpeta `project's_name` y creamos la carpeta `settings` e ingresamos en ella
    md settings
    cd settings
### 12. Dentro de la carpeta `settings` crearemos 5 archivos (`__init__.py, local.py, production.py, base.py, db.py`), en cada creacion apretaremos las teclas (`CTRL + C`) para terminar la creacion de cada archivo `.py`
    copy con __init__.py
    copy con base.py
    copy con db.py
    copy con local.py
    copy con production.py
### 13. Para el codigo del archivo `base.py`, se debe copiar el codigo de `project's_name/settings.py`, ir quitando el siguiente codigo dentro de `base.py`
    from pathlib import Path

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []

    # Database
    # https://docs.djangoproject.com/en/4.1/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.1/howto/static-files/

    STATIC_URL = 'static/'
### 14. Codigo del archivo `db.py`, podemos agregar configuracion de conexion a varias Base de datos, pero por default se usara `SQLITE` en el archivo `local.py` en nuestro local o `production.py` en el servidor donde despleguemos el proyecto
    from pathlib import Path

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # sqlite

    SQLITE = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

    # psycopg2

    """ POSTGRESQL = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'apolo',
            'USER': 'postgres',
            'PASSWORD': '123',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    } """

    # mysqlclient

    """ MYSQL = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'db',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306',
            'OPTIONS': {
                'sql_mode': 'traditional',
            }
        }
    } """
### 15. Codigo del archivo `local.py`
    from .base import *
    from config.settings import db

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []

    # Database
    # https://docs.djangoproject.com/en/4.1/ref/settings/#databases

    DATABASES = db.SQLITE # db.SQLITE # db.POSTGRESQL # db.MYSQL


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.1/howto/static-files/

    STATIC_URL = 'static/'

    # STATICFILES_DIRS = (BASE_DIR, 'static') # STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
    # MEDIA_URL = '/media/'
    # MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
### 16. Codigo del archivo `production.py`
    from .base import *
    from settings import db

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    ALLOWED_HOSTS = []

    # Database
    # https://docs.djangoproject.com/en/3.1/ref/settings/#databases

    DATABASES = db.SQLITE # db.SQLITE # db.POSTGRESQL # db.MYSQL


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.1/howto/static-files/

    STATIC_URL = 'static/'
### 17. Una vez teniendo `base.py` configurado, se deberá eliminar el archivo `project's_name/settings.py`
    cd ..
    del /f /a settings.py
### 18. Regresamos a la carpeta raiz ejecutando dos veces el comando de retroceso
    cd ..
    cd ..
### 19. Dentro del archivo `manage.py`, agregaremos `.local` o `.production` dependiendo si estamos en nuestro local o en el servidor donde despleguemos el proyecto, en la linea de codigo `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project's_name.settings')`, quedando de esta manera el archivo
    #!/usr/bin/env python
    """Django's command-line utility for administrative tasks."""
    import os
    import sys


    def main():
        """Run administrative tasks."""
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project's_name.settings.local') # 'project's_name.settings.local'  # 'project's_name.settings.production'
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        execute_from_command_line(sys.argv)


    if __name__ == '__main__':
        main()
### 20. Dentro del archivo `project's_name/asgi.py`, agregaremos `.local` o `.production` dependiendo si estamos en nuestro local o en el servidor donde despleguemos el proyecto, en la linea de codigo `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project's_name.settings')`, quedando de esta manera el archivo
    """
    ASGI config for config project.

    It exposes the ASGI callable as a module-level variable named ``application``.

    For more information on this file, see
    https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
    """

    import os

    from django.core.asgi import get_asgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project's_name.settings.local') # 'project's_name.settings.local'  # 'project's_name.settings.production'

    application = get_asgi_application()
### 21. Dentro del archivo `project's_name/wsgi.py`, agregaremos `.local` o `.production` dependiendo si estamos en nuestro local o en el servidor donde despleguemos el proyecto, en la linea de codigo `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project's_name.settings')`, quedando de esta manera el archivo
    """
    WSGI config for config project.

    It exposes the WSGI callable as a module-level variable named ``application``.

    For more information on this file, see
    https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
    """

    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project's_name.settings.local') # 'project's_name.settings.local'  # 'project's_name.settings.production'

    application = get_wsgi_application()
### 22. Ejecutar la `migrate` para crear la base de datos SQLite y crear las tablas que vienen por default en Django
    cd ..
    python manage.py migrate

<a name="run_server"></a>

### 23. Correr el Servidor y navegue a `http://localhost:8000` en el navegador, para detener el Servidor (`CTRL + C`), tambien se puede navegar en otro puerto ej: 3000
    python manage.py runserver
    python manage.py runserver 3000
### 24. Para obtener un listado de todos los comandos que se pueden ejecutar con `manage.py`
    python manage.py --help
### 25. Estando dentro del archivo `project's_name/settings/base.py` separaremos en 3 variables la variable `INSTALLED_APPS` y registramos la app `core.app_name` dentro de la variable `LOCAL_APPS`, dejamos comentado la variable `THIRD_APPS` hasta tener apps de terceros instaladas.
    BASE_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

    LOCAL_APPS = [
        'core.app_name'
    ]

    '''THIRD_APPS = [
        
    ]'''

    INSTALLED_APPS = BASE_APPS + LOCAL_APPS '''+ THIRD_APPS'''
### 26. Creacion de `Mapeo Objeto-Relacional (ORM)` a través de `Clases` dentro del archivo `core/app_name/models.py`, en lugar de escribir consultas SQL, aunque podemos usar consultas SQL para los casos mas complejos
    from django.db import models

    # Create your models here.

    class Todo(models.Model):
        created = models.DateTimeField(auto_now_add=True)
        title = models.CharField(max_length=120)
        description = models.TextField()
        completed = models.BooleanField(default=False)
        owner = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE)

        def _str_(self):
            return self.title
### 27. Detenemos el servidor (`CTRL + C`) ya que al agregar, modificar o quitar codigo dentro del archivo `core/app_name/models.py` se deberá ejecutar los siguientes dos comandos para crear un archivo de migracion y para aplicarlos en la base de datos
    python manage.py makemigrations
    python manage.py migrate
### 28. Para probar el CRUD del `modelo (tabla)` creado, se deberá agregar este `modelo` en el archivo `core/app_name/admin.py`
    from django.contrib import admin
    from .models import Todo

    class TodoAdmin(admin.ModelAdmin):
        list_display = ('title', 'description', 'completed')

    # Register your models here.

    admin.site.register(Todo, TodoAdmin)
### 29. Creación de la cuenta `superuser` para acceder a la interfaz de administración
    python manage.py createsuperuser

    Username (leave blank to use 'Computer_UserName'): superuser_name
    Email address: personal_email
    Password: password_we_want_to_use
    Password (again): confirm_password
    Superuser created successfully.
### 30. Agregamos el `PATH` de la vista `ADMIN` en el archivo `project's_name/urls.py`
    from django.contrib import admin
    from django.urls import path

    urlpatterns = [
        path('admin/', admin.site.urls), # Page Admin
    ]
### 31. Volvemos a correr el servidor e ingresamos a la ruta `http://localhost:8000/admin`, deberemos iniciar sesion como `superuser` con el nombre y contraseña que asignamos, para poder ingresar a la interfaz y realizar el CRUD (crear, leer, actualizar, borrar)
    python manage.py runserver

<a name="config_drf"></a>

### 32. Detenemos el servidor (`CTRL + C`) para poder configurar la [DJANGO REST FRAMEWORK](https://www.django-rest-framework.org/#installation) instalando `djangorestframework` y `django-cors-headers`, el ultimo nos sirve para poder evitar errores debidos a las reglas CORS y acortar la url
    py -m pip install djangorestframework django-cors-headers markdown django-filter pygments
### 33. Descomentamos y agregamos los modulos dentro de la variable `THIRD_APPS` que creamos dentro del archivo `project's_name/settings/base.py`
    THIRD_APPS = [
        'rest_framework',
        'corsheaders',
    ]

    INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS
### 34. Agregamos el `PATH` en el archivo `project's_name/urls.py` para poder loguear y desloguearse desde la interfaz que ofrece `DJANGO REST FRAMEWORK`
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path('admin/', admin.site.urls), # Page Admin
        path('api-auth/', include('rest_framework.urls')), # Page log in and Log out Django Rest Framework Authentication Sesion
    ]
### 35. Creamos una carpeta `core/app_name/api` en la cual creamos dentro de ella dos archivos (`routers.py` y `urls.py`) y 4 carpetas (`api/serializers`, `api/viewsets`, `api/filters`, `api/permissions`) creando los archivos respectivos dentro de cada carpeta
    cd core/app_name
    md api
    cd api
    copy con routers.py
    copy con urls.py
    md filters
    cd filters
    copy con app_name_filters.py
    cd ..
    md permissions
    cd viewsets
    copy con app_name_permissions.py
    cd ..
    md viewsets
    cd viewsets
    copy con app_name_viewsets.py
    cd ..
    md serializers
    cd serializers
    copy con app_name_serializers.py
    cd ..
    cd ..
    cd ..
    cd ..
### 36. Estando en la carpeta raiz, debemos agregar el codigo correspondiente en el archivo `core/app_name/serializers/app_name_serializers.py`
    from rest_framework import serializers
    from core.todo.models import Todo

    # Para convertir los datos de la base de datos en objeto JSON
    class TodoSerializer(serializers.ModelSerializer):
        owner = serializers.ReadOnlyField(source='owner.username')

        class Meta:
            model = Todo
            fields = '__all__'
### 37. Agregar el codigo correspondiente en el archivo `core/app_name/api/permissions/app_name_permissions.py`
    from rest_framework import permissions

    # Para dar Acceso de solo lectura, si no esta logueado y no es el usuario quien creo el dato
    class IsOwnerOrReadOnly(permissions.BasePermission):
        """
        Custom permission to only allow owners of an object to edit it.
        """

        def has_object_permission(self, request, view, obj):
            # Read permissions are allowed to any request,
            # so we'll always allow GET, HEAD or OPTIONS requests.

            # Condicion para poder ver el detalle de cada objeto aunque no sea el usuario quien lo creo
            if request.method in permissions.SAFE_METHODS:
                return True

            # Condicion para poder modificar y eliminar el objeto solo el usuario quien lo creo
            # Write permissions are only allowed to the owner of the snippet.
            return obj.owner == request.user
### 38. Agregar el codigo correspondiente en el archivo `core/app_name/api/filters/app_name_filters.py`
    from rest_framework import filters

    # Para dar filtro de datos creados por usuario
    class IsOwnerFilterBackend(filters.BaseFilterBackend):
        """
        Filter that only allows users to see their own objects.
        """
        def filter_queryset(self, request, queryset, view):
            return queryset.filter(owner=request.user)

    class IsOwnerFilterBackendUsers(filters.BaseFilterBackend):
        """
        Filter that only allows users to see their own objects.
        """
        def filter_queryset(self, request, queryset, view):
            return queryset.filter(pk=request.user.id)

### 39. Agregar el codigo correspondiente en el archivo `core/app_name/api/viewsets/app_name_viewsets.py`
    from rest_framework import permissions viewsets
    from core.todo.models import Todo
    from core.todo.api.permissions.todo_permissions import IsOwnerOrReadOnly
    from core.todo.api.serializers.todo_serializers import TodoSerializer
    from core.todo.api.filters.todo_filters import IsOwnerFilterBackend

    # Para proporcionar los metodos REQUESTS sin necesitas de crear cada uno de ellos desde cero, al igual el uso de permisos y autentificaciones
    class TodoViewSet(viewsets.ModelViewSet):
        """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.

        Additionally we also provide an extra `highlight` action.

        IsAuthenticatedOrReadOnly -> Está autenticado o es de solo lectura \n
        IsAuthenticated -> Está autenticado \n
        AllowAny -> Permitir Cualquiera \n
        IsOwnerOrReadOnly -> Si es el creador del objeto, si no solo lectura \n
        IsOwnerFilterBackend -> Se filtrara solo sus objetos creados por el
        """
        queryset = Todo.objects.all() # queryset -> lista de objetos de un modelo determinado
        serializer_class = TodoSerializer
        permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] # Si no esta auntentificado, solo puede ver los datos, Si el detalle de los datos no los creo el usuario auntentificado solo podra verlos
        filter_backends = [IsOwnerFilterBackend] # filtra solo los datos creador por el usuario autentificado

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)
### 40. Agregar el codigo correspondiente al archivo `core/app_name/api/routers.py`
    from rest_framework.routers import DefaultRouter
    from core.todo.api.viewsets import todo_viewsets

    # Create a router and register our viewsets with it.
    router = DefaultRouter()

    # Los routers nos proporciona dos path para la lista de los objetos creados y el detalle de cada uno sin la necesidad de crearlos desde ceros cada uno
    router.register(r'snippets', todo_viewsets.SnippetViewSet, basename="snippet")
    router.register(r'users', todo_viewsets.UserViewSet, basename="user")
    router.register(r'todos', todo_viewsets.TodoViewSet, basename="todo")
### 41. Agregar el codigo correspondiente al archivo `core/app_name/api/urls.py`, para acceder a la `url` donde generaremos el token del usuario logueado y el `router` para crear y acceder a la lista y detalles de los objetos
    from django.urls import path
    from core.todo.api.routers import router
    from rest_framework.authtoken.views import obtain_auth_token

    # The API URLs are now determined automatically by the router.
    urlpatterns = [
        path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # Generator token authentication
    ]

    # Agregamos al path anterior, los path creados en el archivo routers.py
    urlpatterns += router.urls
### 42. Agregamos `'rest_framework.authtoken'` en la variable `THIRD_APPS`, separamos la variable `MIDDLEWARE` y agregamos `'corsheaders.middleware.CorsMiddleware'` en la nueva variable `THIRD_MIDDLEWARE`, creamos la variable `REST_FRAMEWORK` para agregar las propiedades demanera globales para `DJANGO REST FRAMEWORK` y por ultimo creamos la variable `CORS_ORIGIN_WHITELIST` para asignar la url del servidor donde se encuentra la app quien usará la `API` dentro del archivo `project's_name/settings/base.py` para poder generar token por usuario, usarlo para la autenticacion por token y acceder a la `API REST`
    THIRD_APPS = [
        'rest_framework',
        'corsheaders',
        'rest_framework.authtoken',
    ]

    BASE_MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    THIRD_MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
    ]

    MIDDLEWARE = BASE_MIDDLEWARE + THIRD_MIDDLEWARE

    # Django REST Framework
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication',
        ],
    }

    CORS_ORIGIN_WHITELIST = [
        'http://localhost:5173'
    ]
### 43. Ejecutamos el comando de migracion para poder crear las tablas que almacenaran los tokens de autenticacion, las cuales vienen con la importacion de la app `'rest_framework.authtoken'`
    python manage.py migrate
### 44. Agregamos `path('', include('core.app_name.api.urls')),` al archivo general `project's_name/urls.py` para poder acceder a las `urls` de `list` y `detail`
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path('admin/', admin.site.urls), # Page Admin
        path('api-auth/', include('rest_framework.urls')), # Page log in and Log out Django Rest Framework Authentication Sesion
        path('', include('core.todo.api.urls')), # Pages (General, List snippets, Details snippet, List user, Details user, List todo, Details todo, generator token api-token-auth)
    ]
### 45. Ejecutamos nuevamente el servidor
    python manage.py runserver

[Subir](#top)
<a name="creation_requirements"></a>
<a name="dependencias"></a>

## [Creacion](https://www.youtube.com/watch?v=90YKt9PlWZY) de archivo `requirements.txt` e [Instalacion](https://gist.github.com/kamikaze-lab/7d5987ff86223e1bf686) de estas dependencias

### 1. Para crear el archivo que especifica las dependencias requeridas para usar este proyecto y para la instalacion de las dependencias
    pip freeze > requirements.txt
    pip install -r requirements.txt

