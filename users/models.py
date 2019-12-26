
#https://docs.djangoproject.com/en/2.2/topics/auth/customizing/

# Create your models here.

#Aca vamos a crear una tabla para los campos adicionales que Django no contiene # -*- coding: utf-8 -*-
#su tabla auth_user

from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
#Modelo de perfil
#Modelo proxy que extiende la base de datos con otra info

#https://docs.djangoproject.com/en/2.2/ref/models/fields/
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200,blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    created = models.DateField(auto_now_add = True)
    modified = models.DateField(auto_now = True)

    def __str__(self):
        #Devuelve username
        return self.user.username
