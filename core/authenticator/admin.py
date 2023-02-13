from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'nick_name', 'first_name', 'last_name', 'registration_date')

# Register your models here.

admin.site.register(User, UserAdmin)