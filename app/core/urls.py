# Django
from django.urls import path

# Views
from core.views import IndexView

app_name = 'core'

urlpatterns = [
    
    # Index
    path('',  IndexView.as_view(), name='monitora-index'),

]