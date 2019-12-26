# URLS de usuarios

# Django
from django.urls import path
#https://docs.djangoproject.com/en/2.1/topics/class-based-views/#simple-usage-in-your-urlconf
#https://ccbv.co.uk/

# Views
from users import views

urlpatterns = [

    #Posts
    path(
        route='<str:username>/', #este es el kwarg (key word argument)
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    # Administración
    path(
        route='login/', 
        view=views.login_view, 
        name='login'
    ),
    path(
        route='logout/', 
        view=views.logout_view, 
        name='logout'
    ),
    path(
        route='signup/', 
        view=views.signup, 
        name='signup'
    ),
    path(
        route='me/profile/', 
        view=views.update_profile, 
        name='update'
    )

]
