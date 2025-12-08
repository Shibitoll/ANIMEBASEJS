# anime_api/tests/test_serializers.py

from django.test import TestCase
from anime_api.models import Anime
from anime_api.serializers import AnimeSerializer

class AnimeSerializerTest(TestCase):

    def setUp(self):
        self.anime = Anime.objects.create(
            title="Клинок, що винищує демонів",
            year=2019,
            episodes="44 eps",
            rating=8.7, # R1.5
            genres="Екшн, Надприродне",
            description="Тест серіалізатора.",
            status="Ongoing",
            image_url="https://static.yani.tv/posters/full/1636692030.jpg",
            is_featured=True
        )
        self.serializer = AnimeSerializer(instance=self.anime)

    def test_serializer_output_fields(self):
        """R1.3: Перевірка, що серіалізатор містить всі ключові поля для деталізації."""
        data = self.serializer.data
        
        self.assertIn('description', data)
        self.assertIn('episodes', data)
        self.assertIn('genres', data)

    def test_serializer_data_content(self):
        """R1.3, R1.5: Перевірка коректності переданих значень (рейтинг, назва, статус)."""
        data = self.serializer.data
        
        self.assertEqual(data['title'], "Клинок, що винищує демонів")
        self.assertEqual(data['rating'], '8.7')
        self.assertEqual(data['status'], 'Ongoing')