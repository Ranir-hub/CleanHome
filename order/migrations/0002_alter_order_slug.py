# Generated by Django 5.2.1 on 2025-06-09 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
