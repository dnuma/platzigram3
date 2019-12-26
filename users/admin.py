# Clases de usuarios administrador

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# Register your models here.
from users.models import Profile


#Forma rápida, poco práctica:
#admin.site.register(Profile)

@admin.register(Profile) #malparidos decoradores
class ProfileAdmin(admin.ModelAdmin):
#Perfil de administrador
# https://docs.djangoproject.com/es/2.2/ref/contrib/admin/
# https://docs.djangoproject.com/en/2.2/topics/auth/customizing/
    list_display = (
        'pk',
        'user',
        'phone_number',
        'website',
        'picture'
    )

    list_display_links = (
        'pk',
        'user'
    )

    list_editable = (
        'phone_number',
        'website',
        'picture'
    )
#no se puede sólo user porque es una relación, no es un campo
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )

    fieldsets = (
        ('Perfil', {
            #'fields': ('user', 'picture'), probar con esta tupla simple
            'fields': (
                ('user', 'picture'),
            ),
        }),

        ('Info extra', {
            'fields': (
                ('website','phone_number'),
                ('biography')
            ),
        }),

        ('Metadata',{
            'fields': ('created','modified'),
        })
    )

    readonly_fields = (
        'created',
        'modified',
        'user'
    )

class ProfileInline(admin.StackedInline):
#A partir de acá es para meter los campos personalizados que creamos
#en la creación de usuarios

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
#Añadir perfil de admin al administrador de usuarios
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
