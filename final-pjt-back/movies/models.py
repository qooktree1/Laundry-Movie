from django.db import models

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    genres = models.ManyToManyField(Genre, related_name="genre")

    title = models.CharField(max_length=100)
    release_date = models.DateField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    video_path = models.CharField(max_length=200)
    runtime = models.IntegerField()