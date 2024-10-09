# administracion/views.py
from django.shortcuts import render

def login_view(request):
    return render(request, 'administracion/login.html')
