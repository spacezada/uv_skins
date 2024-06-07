from django.urls import path
from . import views

urlpatterns = [
    path('', views.skin_list, name='skins_list'),
    path('contato/', views.contato, name='contato'),
]