# Django
from django.urls import path

# Views
from core.views import *

app_name = 'core'

urlpatterns = [
    
    # Rotas
    path('',  IndexView.as_view(), name='index'),
    path('biography/',  BiographyView.as_view(), name='biography'),

    # Dark Mode
    path('dark-mode/',  DarkModeView.as_view(), name='dark-mode'),

]