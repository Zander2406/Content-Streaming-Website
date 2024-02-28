from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=15)


class Lang(models.Model):
    name = models.CharField(max_length=10)


class Type(models.Model):
    name = models.CharField(max_length=10)


class Status(models.Model):
    name = models.CharField(max_length=10)


class Year(models.Model):
    year = models.IntegerField()


class Season(models.Model):
    name = models.CharField(max_length=20)


class Episodes(models.Model):
    name = models.CharField(max_length=30)
    episode_link = models.CharField(max_length=200)


class Anime(models.Model):
    anime_banner_link = models.CharField(max_length=200)
    type = models.ForeignKey('Type', on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=2000)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
    released = models.ForeignKey('Year', on_delete=models.CASCADE, null=False)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)
    other_names = models.CharField(max_length=200)
