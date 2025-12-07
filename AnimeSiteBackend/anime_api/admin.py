# AnimeSiteBackend/anime_api/admin.py

from django.contrib import admin
from .models import Anime

# Реєстрація моделі Anime
@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    # Відображення полів у списку адміністратора
    list_display = ('title', 'year', 'rating', 'status', 'is_featured')
    # Фільтр за статусом та чи є аніме рекомендованим
    list_filter = ('status', 'is_featured')
    # Пошук за назвою та жанрами
    search_fields = ('title', 'genres')