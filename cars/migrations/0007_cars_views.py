# Generated by Django 5.1.1 on 2024-10-01 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_networklink_cars'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
    ]
