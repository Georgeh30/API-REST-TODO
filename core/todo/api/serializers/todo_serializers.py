# CODE TO https://www.django-rest-framework.org/tutorial/quickstart/
from core.todo.models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title','description','completed')



""" # CODE TO https://www.youtube.com/watch?v=GE0Q8YNKNgs
from rest_framework import serializers
from core.todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title','description','completed') """



""" # CODE TO https://gitlab.com/wdavilav/apolo/-/blob/master/core/api/serializers.py
from rest_framework import serializers
from core.todo.models import Todo


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__' """
