# https://docs.djangoproject.com/en/3.0/topics/auth/default/#auth-web-requests

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
#para que no haga logout de una sesión inexistente se usa el decorador login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, TemplateView

#para registro de usuarios
#https://docs.djangoproject.com/en/2.2/topics/auth/default/

from users.models import Profile

#Excepciones
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from posts.models import Post

#Forms
from users.forms import ProfileForm, SignUpForm

# Create your views here.

# https://docs.djangoproject.com/en/2.2/topics/http/middleware/
# https://docs.djangoproject.com/en/2.2/topics/forms/
# https://docs.djangoproject.com/en/2.2/ref/forms/fields/


class UserDetailView(LoginRequiredMixin,DetailView):
    #Detalle de vista de usaurios

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username' # kwarg = key word argument. Del urls.py 
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        #Añade post de usuarios al contexto
        #https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-display/#detailview
        context = super().get_context_data(**kwargs)
        user = self.get_object() #es el método que se encarga de hacer el queqry del object seguún los parámetros enviados
        #para mostrar los post del mismo usuario en orden ascendente
        context['posts'] = Post.objects.filter(user=user).order_by('-created') 
        return context

@login_required
def update_profile(request):

    profile = request.user.profile 

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            #reverse construye una URL
            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url) #el navegador siempre debe redireccionar a algún lado
    else:
        form = ProfileForm()


    return render(
        request = request,
        template_name = 'users/update_profile.html',
        context = {
            'profile': profile,
            'user': request.user,
            'form': form
        })


def login_view(request):
    
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            # lo trae de users/urls.py
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html',{'error': 'Nombre de usuari o contraseña inválido'})

    return render(request, 'users/login.html')


# https://docs.djangoproject.com/en/2.2/topics/auth/default/
def signup(request):
    # Vista de sign up
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignUpForm()
    
    return render(
        request=request,
        template_name = 'users/signup.html',
        context={'form': form}
    )


@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')


"""
#! Método antiguo, ya se usa con class para no ver todo esto en el código
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request,'users/signup.html', {'error': 'Password confirmation does not match'})
        
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username already in use'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')


    return render(request, 'users/signup.html') 
"""

