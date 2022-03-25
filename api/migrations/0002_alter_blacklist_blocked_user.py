# Generated by Django 3.2.7 on 2021-11-16 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blacklist',
            name='blocked_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_who_blocked_you', to=settings.AUTH_USER_MODEL),
        ),
    ]