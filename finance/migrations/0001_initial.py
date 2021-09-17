# Generated by Django 3.2.4 on 2021-09-07 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.CharField(default=0, max_length=255, verbose_name='Баланс')),
                ('price_of_all_indexes', models.CharField(default=0, max_length=255, verbose_name='Цена всех индексов')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField(auto_now_add=True, db_index=True, verbose_name='Дата покупки')),
                ('state', models.CharField(max_length=255, verbose_name='Статус')),
                ('name', models.CharField(max_length=255, verbose_name='Название индекса')),
                ('price', models.CharField(default=0, max_length=255, verbose_name='Цена')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
