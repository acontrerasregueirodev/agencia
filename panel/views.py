# panel/views.py

from django.shortcuts import render
from django.contrib import messages

def admin_panel(request):
    # Aquí puedes agregar la lógica específica para el panel del administrador
    messages.success(request, 'Bienvenido al panel de administrador!')
    return render(request, 'panel/admin_panel.html')

def manager_panel(request):
    # Aquí puedes agregar la lógica específica para el panel del manager
    messages.success(request, 'Bienvenido al panel de manager!')
    return render(request, 'panel/manager_panel.html')
