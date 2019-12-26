# Catalogo de middleware de Platzigram

from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    #Ensure every user is interacting with the platform have their profile pic and bio

    def __init__(self, get_response):
        #inicialización de middleware
        self.get_response = get_response

        
    def __call__(self, request):
        #código que se ejecuta cada que se llama el view
        if not request.user.is_anonymous: #propiedad del middleware
            if not request.user.is_staff:
                profile = request.user.profile #trae todo los elementos del profile
                if not profile.picture or not profile.biography:
                    #para evitar redireccionamiento eterno error 302 se usa esto
                    if request.path not in [reverse('users:update_profile'), reverse('users:logout')]: 
                        return redirect('users:update_profile')
        response = self.get_response(request)
        return response
