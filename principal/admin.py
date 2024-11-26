from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Perfil

# Registra el modelo de Usuario personalizado
admin.site.register(Usuario, UserAdmin)
admin.site.register(Perfil)