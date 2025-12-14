# anime_api/views.py
from rest_framework import viewsets
from .models import Anime
from .serializers import AnimeSerializer

class AnimeViewSet(viewsets.ReadOnlyModelViewSet):
    # Додавання .select_related() або .prefetch_related() тут покращить продуктивність,
    # але для цієї лабораторної роботи залишаємо просте рішення.
    queryset = Anime.objects.all().order_by('-id') 
    serializer_class = AnimeSerializer