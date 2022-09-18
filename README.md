# API-REST-TODO
REST API created with DJANGO API REST FRAMEWORK for the use of the TO DO web application where the only data is the task title and its description

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
### 5. Asegurando que esta activo el Entorno Vitual, Instalaremos el [Framework Django](https://docs.djangoproject.com/es/4.1/topics/install/#installing-official-release)
    py -m pip install Django
### 6. Verificamos que la terminal detecte el Framework Django, mostrando la version instalada, en caso de no detectar el modulo `django`, desinstalaremos el modulo y lo volvemos a instalar, para volver a validar la version del modulo.
    python -m django --version
    py -m pip uninstall Django
    py -m pip install Django
### 7. Creacion del nuevo proyecto [Django](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react)
    django-admin startproject project's_name .
### 8. Creacion de una nueva aplicacion
    python manage.py startapp app_name
### 9. Ejecutar la `migrate` para crear la base de datos SQLite y crear las tablas que vienen por default en Django
    python manage.py migrate
### 10. Correr el Servidor y navegue a `http://localhost:8000` en el navegador, para detener el Servidor (`CTRL + C`)
    python manage.py runserver
