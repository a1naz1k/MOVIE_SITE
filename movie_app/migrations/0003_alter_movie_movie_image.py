# Generated by Django 5.1.3 on 2024-12-01 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_alter_moments_movie_moments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_image',
            field=models.ImageField(blank=True, null=True, upload_to='movie_images/'),
        ),
    ]
