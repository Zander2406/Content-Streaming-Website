# Generated by Django 4.1.1 on 2024-03-10 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_anime_lang'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genremap',
            old_name='anime_id',
            new_name='anime',
        ),
        migrations.RenameField(
            model_name='genremap',
            old_name='genre_id',
            new_name='genre',
        ),
    ]
