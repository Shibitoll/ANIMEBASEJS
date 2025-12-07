# anime_api/models.py
from django.db import models

class Anime(models.Model):
    STATUS_CHOICES = [
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=100)
    year = models.IntegerField()
    episodes = models.CharField(max_length=10) # '44 eps', '1 eps', '1000 eps'
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    genres = models.CharField(max_length=100) # Розділені комою: 'Action, Supernatural'
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    # зберігає шлях до зображення або URL
    image_url = models.CharField(max_length=200, default='default.jpg')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title