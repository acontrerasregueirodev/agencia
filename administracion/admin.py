from django.contrib import admin
from .models import Admin, Manager

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'admin')  # Asegúrate de que 'admin' esté aquí
    list_filter = ('admin',)  # Cambia 'administrador' a 'admin'

admin.site.register(Admin)
admin.site.register(Manager, ManagerAdmin)