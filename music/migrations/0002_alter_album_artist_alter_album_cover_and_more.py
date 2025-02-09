# Generated by Django 5.0.4 on 2024-05-04 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='music.artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.URLField(null=True),
        ),
    ]
