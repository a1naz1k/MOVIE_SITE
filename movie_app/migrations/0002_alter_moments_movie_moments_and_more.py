# Generated by Django 5.1.3 on 2024-12-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moments',
            name='movie_moments',
            field=models.ImageField(blank=True, null=True, upload_to='movie_moments/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_trailer',
            field=models.FileField(blank=True, null=True, upload_to='movie_trailers/'),
        ),
        migrations.AlterField(
            model_name='movielanguages',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='movie_languages/'),
        ),
    ]
