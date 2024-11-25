import requests
from django.shortcuts import render

def obtener_anime(request):
    url = 'http://localhost:3000/anime/gogoanime/search'
    params = {'query': 'One Piece'}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        anime_data = response.json().get('results', [])  # Obtener los resultados
        print(f"Datos obtenidos de la API: {anime_data}")  # Imprimir datos obtenidos
    except requests.exceptions.RequestException as e:
        anime_data = []
        print(f"Error al conectar con la API de Consumet: {e}")

    context = {
        'anime_data': anime_data
    }
    return render(request, 'anime/anime.html', context)
