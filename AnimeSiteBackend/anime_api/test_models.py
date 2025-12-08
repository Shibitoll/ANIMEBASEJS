# anime_api/tests/test_models.py

from django.test import TestCase
from anime_api.models import Anime
# from django.core.exceptions import ValidationError # Не використовується в цьому коді

class AnimeModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.anime = Anime.objects.create(
            title="Атака Титанів",
            year=2013,
            episodes="87 eps",
            rating=9.0, # R1.5, R1.3
            genres="Екшн, Драма, Військовий",
            description="Models test",
            status="Completed",
            image_url="https://cdn.europosters.eu/image/hp/65791.jpg",
            is_featured=True # R1.2
        )

    def test_anime_title_and_year_content(self):
        """R1.3: Перевірка, що основні поля відображаються коректно."""
        self.assertEqual(self.anime.title, "Атака Титанів")
        self.assertEqual(self.anime.year, 2013)

    def test_string_representation(self):
        """R1.3: Перевірка, що метод __str__ повертає назву аніме."""
        self.assertEqual(str(self.anime), self.anime.title)

    def test_featured_status(self):
        """R1.2: Перевірка коректності статусу 'featured'."""
        self.assertTrue(self.anime.is_featured)

def test_is_ongoing_status_creation(self):
        """R1.4: Перевірка, що статус 'Ongoing' коректно зберігається."""
        
        # ДОДАНО year, episodes, rating та інші обов'язкові поля
        ongoing_anime = Anime.objects.create(
            title="Ongoing Test", 
            status="Ongoing",
            year=2024,         
            episodes="1 ep",    
            rating=5.0,        
        ) 
        self.assertEqual(ongoing_anime.status, "Ongoing")