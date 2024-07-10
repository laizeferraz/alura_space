# Generated by Django 5.0.6 on 2024-07-10 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_alter_pictures_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='category',
            field=models.CharField(choices=[('NEBULAE', 'Nebulae'), ('GALAXY', 'Galaxy'), ('STAR', 'Star'), ('PLANET', 'Planet')], default='NEBULAE', max_length=100),
        ),
    ]
