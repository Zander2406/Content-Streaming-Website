# Generated by Django 4.1.1 on 2024-03-17 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_rename_anime_id_genremap_anime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]