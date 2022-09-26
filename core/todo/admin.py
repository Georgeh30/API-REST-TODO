""" from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(Todo, TodoAdmin) """

from django.contrib import admin
from .models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('created', 'title', 'code', 'linenos', 'language', 'style')

# Register your models here.

admin.site.register(Snippet, SnippetAdmin)