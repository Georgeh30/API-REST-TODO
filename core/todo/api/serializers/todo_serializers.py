from rest_framework import serializers
from core.todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title','description','completed')

""" from rest_framework import serializers
from core.todo.models import Todo


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__' """
