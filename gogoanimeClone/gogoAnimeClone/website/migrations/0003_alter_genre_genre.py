# Generated by Django 4.1.1 on 2024-03-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_anime_genre_genremap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(max_length=30),
        ),
    ]