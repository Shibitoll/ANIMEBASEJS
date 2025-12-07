# AnimeSiteBackend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from anime_api.views import AnimeViewSet

# Імпорт для обслуговування медіафайлів у режимі розробки
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'anime', AnimeViewSet) # /api/v1/anime/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)), # API-endpoints
]

# Обслуговування медіафайлів тільки в режимі DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)