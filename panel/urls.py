# panel/urls.py

from django.urls import path
from .views import admin_panel, manager_panel

urlpatterns = [
    path('admin_panel/', admin_panel, name='admin_panel'),  # Vista del panel de administrador
    path('manager_panel/', manager_panel, name='manager_panel'),  # Vista del panel de manager
]

