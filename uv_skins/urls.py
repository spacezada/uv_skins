from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('skins/', include('skins.urls')),
    path('users/', include('users.urls')),
    
]