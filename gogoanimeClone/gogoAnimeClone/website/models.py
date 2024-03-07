from django.db import models


class Genre(models.Model):
    genre = models.CharField(max_length=30)


class Lang(models.Model):
    lang = models.CharField(max_length=10)


class Type(models.Model):
    type = models.CharField(max_length=10)


class Status(models.Model):
    status = models.CharField(max_length=10)


class Year(models.Model):
    year = models.IntegerField()


class Season(models.Model):
    season = models.CharField(max_length=20)
    year = models.ForeignKey('Year', on_delete=models.CASCADE, null=False)


class Episodes(models.Model):
    name = models.CharField(max_length=30)
    episode_link = models.CharField(max_length=200)
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE, null=False)


class Anime(models.Model):
    anime_banner_link = models.CharField(max_length=200)
    type = models.ForeignKey('Type', on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=200)
    summary = models.TextField()
    released = models.ForeignKey('Season', on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)
    other_names = models.TextField()


class GenreMap(models.Model):
    genre_id = models.ForeignKey('Genre', on_delete=models.CASCADE, null=True)
    anime_id = models.ForeignKey('Anime', on_delete=models.CASCADE, null=True)
