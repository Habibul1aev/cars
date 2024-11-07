# Generated by Django 5.1.1 on 2024-09-24 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_networklink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networklink',
            name='cars',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='cars.cars'),
        ),
    ]
