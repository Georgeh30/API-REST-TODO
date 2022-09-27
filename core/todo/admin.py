""" from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(Todo, TodoAdmin) """

from django.contrib import admin
from .models import Snippet, Todo

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('created', 'title', 'code', 'linenos', 'language', 'style')

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Todo, TodoAdmin)