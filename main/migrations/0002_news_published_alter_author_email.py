# Generated by Django 4.0.6 on 2022-07-26 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
