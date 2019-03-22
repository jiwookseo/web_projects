from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=30, default='')
    audience = models.IntegerField(default=0)
    poster_url = models.CharField(max_length=140, default='')
    description = models.TextField(default='')
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, default=None)


class Score(models.Model):
    content = models.CharField(max_length=140, default='')
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=None)
