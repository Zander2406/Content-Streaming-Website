# Generated by Django 4.1.1 on 2024-05-31 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_episodes_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='name_slug',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
