# Generated by Django 4.2 on 2024-05-29 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_inmueble_region_alter_inmueble_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
