from django.db import models
from .Movie import Movie
from .Actor import Actor

class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movi_id')
    user_id = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='user_id')
    text = models.TextField(blank=True, null=True)
    created_date = models.DateField()
