from django.contrib import admin
from django.contrib.auth.decorators import login_required
from modulos.Login.views_login.views_login import *
from django.urls import path

urlpatterns = [
    path('accounts/login/', Login.as_view(), name='login'),
    path('', MainView.as_view(), name='index'),
    path('logout', login_required(LogoutUsuario), name='logout'),
    path('clave_olvidar/', ForgetPassword.as_view(), name='claveolv'),
    path('cambiar_clave/', CambiarPassword.as_view(), name='clavenew')
]
