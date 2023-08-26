from django.urls import path
from .views import *


urlpatterns = [

    path('', user_login, name='login'),
    path('register/', user_registration, name='register'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', user_dashboard, name='dashboard'),
    path('profile/', users_profile, name='profile'),
    path('logout/', user_logout, name='logout'),

    # Pre-module-options-router
    path('pre_options/', user_options_pre, name='pre_options'),
    path('para_options/', user_options_para, name='para_options'),
    path('clinical_options/', user_options_clicnical, name='clinical_options'),

    path('server_updating_files/', db_update, name='server_updating_files'),
]
