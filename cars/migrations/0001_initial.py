# Generated by Django 5.1.1 on 2024-09-21 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=10, verbose_name='Марка')),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Марка')),
                ('photo', models.ImageField(upload_to='imgs/', verbose_name='Фото')),
                ('volume', models.CharField(max_length=3, verbose_name='Объем')),
                ('model', models.CharField(max_length=20, verbose_name='Модель')),
                ('info', models.TextField(verbose_name='Информация')),
                ('data', models.DateField(default='default_value', verbose_name='Дата')),
                ('price', models.CharField(max_length=12, verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='cars.category', verbose_name='категория')),
            ],
        ),
    ]
