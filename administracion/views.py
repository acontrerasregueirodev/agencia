from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  # Cambiado a 'username'
            contraseña = form.cleaned_data['contraseña']
            
            # Intenta autenticar como Admin
            admin = authenticate(request, username=username, password=contraseña)  # Cambiado a 'username'
            if admin is not None:
                login(request, admin)
                return redirect('admin_panel')  # Redirigir a admin_mpanel
            
            # Intenta autenticar como Manager
            manager = authenticate(request, username=username, password=contraseña)  # Cambiado a 'username'
            if manager is not None:
                login(request, manager)
                return redirect('manager_panel')  # Redirigir a managers_panel
            
            messages.error(request, 'Credenciales inválidas')  # Mensaje de error
    else:
        form = LoginForm()
    
    return render(request, 'administracion/login.html', {'form': form})
