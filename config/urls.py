"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    path('', include('core.todo.api.urls')), # CODE TO https://www.django-rest-framework.org/tutorial/quickstart/
    # Esta url sirve para mostrar la opcion de "Log out" en la vista de Django REST Framework
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) # CODE TO https://www.django-rest-framework.org/tutorial/quickstart/



    # path('', include('core.todo.api.urls')), # https://www.youtube.com/watch?v=GE0Q8YNKNgs



    # path('api/', include('core.todo.api.urls')), # https://gitlab.com/wdavilav/apolo/-/blob/master/config/urls.py
]
