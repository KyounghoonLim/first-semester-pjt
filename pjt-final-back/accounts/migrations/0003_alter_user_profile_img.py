# Generated by Django 3.2.9 on 2021-11-23 13:32

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(blank=True, upload_to=accounts.models.profile_image_path),
        ),
    ]
