# Generated by Django 5.1.4 on 2025-01-11 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_alter_review_movie_alter_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(max_length=255),
        ),
    ]
