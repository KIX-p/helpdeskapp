# Generated by Django 4.2.7 on 2023-12-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdeskapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='slug',
            field=models.SlugField(default='default-slug', unique=True),
        ),
    ]
