from django.db import models

# Create your models here.

from django.contrib.auth.models import User

#https://docs.djangoproject.com/en/2.2/ref/models/fields/

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return '{} por @{}'.format(self.title, self.user.username)
        

"""
CREACIÓN DE TABLA PARA USUARIOS (django tiene una auth.user pero este es el ejercicio)
# https://docs.djangoproject.com/en/3.0/intro/overview/
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)

#Cuando se cree instancia en DB, crea la fecha
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

#ejecutar:
# python manage.py makemigrations
# python manage.py migrate
# crea nueva tabla dentro de la DB llamada post_user
# https://docs.djangoproject.com/en/3.0/topics/db/queries/

"""

"""
EN CONSOLA SE PONE ESTO

from posts.models import User
users = [
  {
    'email': 'cvander@platzi.com',
    'first_name': 'Christian',
    'last_name': 'Van Der Henst',
    'password': '1234567',
    'is_admin': True
  },
  {
    'email': 'freddier@platzi.com',
    'first_name': 'Freddy',
    'last_name': 'Vega',
    'password': '987654321'
  },
  {
    'email': 'yesica@platzi.com',
    'first_name': 'Yésica',
    'last_name': 'Cortes',
    'password': 'qwerty',
    'birthdate': date(1990,12,19)
  },
  {
    'email': 'arturo@platzi.com',
    'first_name': 'Arturo',
    'last_name': 'Martinez',
    'password': 'msi',
    'is_admin': True,
    'birthdate': date(1981,11,6),
    'bio': "a la grande le puse cuca. Homero J Simpsons"
  }
]

from posts.models import user

for user in users:
  obj = User(**user)
  obj.save()
  print(obj.pk)


PARA FILTRAR SE PONE ESTA SECUENCIA DE CÓDIGO EN CONSOLA
platzi_users = User.objects.filter(email__endswith='@platzi.com')

Para actualizar algún campo se usa Update, ej convirtiendo todos en admmin:
platzi_users = User.objects.filter(email__endswith='@platzi.com').update(is_admin=True)
con GET no funciona porque devuelve más de 1 valor
platzi_users = User.objects.get(email__endswith='@platzi.com')
"""
