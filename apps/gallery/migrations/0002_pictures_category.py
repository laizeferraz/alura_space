# Generated by Django 5.0.6 on 2024-07-09 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='category',
            field=models.CharField(choices=[('NEBULAE', 'Nebulae'), ('GALAXIES', 'Galaxies'), ('STARS', 'Stars'), ('PLANETS', 'Planets')], default='NEBULAE', max_length=100),
        ),
    ]