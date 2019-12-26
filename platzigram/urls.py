"""
Archivo de URLS de platzigram

"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static  # para poder ver la foto del usuario
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),

 
    # Llama a posts/urls.py cuando se entra al home
    path('', include(('posts.urls','posts'), namespace='posts')),

    # Llama a users/urls.py cuando se entra al home/users/...
    path('users/', include(('users.urls', 'users'), namespace='users')),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #para mostrar la foto

#https://docs.djangoproject.com/en/2.2/ref/settings/
