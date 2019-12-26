#Formularios de Post

#Django
from django import forms

#Models
from posts.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        #Form Settings
        model = Post
        fields = ('user','profile','title','photo')