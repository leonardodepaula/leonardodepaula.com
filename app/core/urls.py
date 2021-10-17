# Django
from django.urls import path

# Views
from core.views import *

app_name = 'core'

urlpatterns = [
    
    # Index
    path('',  IndexView.as_view(), name='index'),

    # Dark Mode
    path('dark-mode/',  DarkModeView.as_view(), name='dark-mode'),

]