# Generated by Django 5.0.6 on 2024-07-09 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_pictures_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]