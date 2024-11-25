
from django.urls import path
from .views import obtener_anime

urlpatterns = [
    path('animeinfo/', obtener_anime, name='obtener_anime'),
]
