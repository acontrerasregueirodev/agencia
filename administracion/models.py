from django.db import models

# Modelo para el Admin
class Admin(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=150)  # Almacenar de forma segura con hash en producción

    def __str__(self):
        return f'Admin: {self.nombre} {self.apellido}'

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'


# Modelo para el Manager
class Manager(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=150)  # Almacenar de forma segura con hash en producción
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='managers')

    def __str__(self):
        return f'Manager: {self.nombre} {self.apellido}'
