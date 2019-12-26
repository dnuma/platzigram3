# https://docs.djangoproject.com/en/3.0/topics/auth/default/#auth-web-requests
# funcion que toma un request

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView  # recibe un modelo
# from django.http import HttpResponse

#Forms
from posts.forms import PostForm

#Models
from posts.models import Post

# Utilities
from datetime import datetime


class PostsFeedView(LoginRequiredMixin, ListView):
    #Muestra todos los posts del usuario

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'post'


class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'


#https://ccbv.co.uk/projects/Django/2.2/django.views.generic.edit/CreateView/

class CreatePostView(LoginRequiredMixin, CreateView):
    #Crea un nuevo post

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
    
    def get_context_data(self, **kwargs):
        #Añade usuario y perfil al contexto
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.profile
        return context
