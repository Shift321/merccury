# Generated by Django 3.2.7 on 2021-11-30 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211116_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='user/profile_photo'),
        ),
    ]
