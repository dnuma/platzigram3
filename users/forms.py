
# django
from django import forms

# models
from django.contrib.auth.models import User
from users.models import Profile

class SignUpForm (forms.Form):
    #Formujlario de registro
    username = forms.CharField(min_length=4, max_length=50)
    #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/ para crear campos específicos
    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70, 
        widget=forms.PasswordInput()
    )
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    # https://docs.djangoproject.com/en/3.0/ref/forms/validation/
    def clean_username(self):
        # nombre de usuario único, se hace a través de query
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError('Nombre de usuario en uso.')
        return username # ! Siempre se debe devolver el nombre de usuario

    def clean(self):
        #Verificación de confirmación de contraseña correcta
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no concuerdan')
        return data

    def save(self):
        #Crea usuario y lo guarda
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


# https://docs.djangoproject.com/en/3.0/ref/forms/fields/
class ProfileForm(forms.Form):
    # formulario de perfil

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number =forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
