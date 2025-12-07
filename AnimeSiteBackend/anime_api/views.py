# anime_api/views.py
from rest_framework import viewsets
from .models import Anime
from .serializers import AnimeSerializer

class AnimeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Anime.objects.all().order_by('-id') # Останні релізи
    serializer_class = AnimeSerializer