# Django
from django.contrib import admin
from django.urls import path, include

# Urls
import core.urls

urlpatterns = [

    # Apps
    path('', include('core.urls')),

    # Admin
    path('admin/', admin.site.urls),

]
