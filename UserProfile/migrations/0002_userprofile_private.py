# Generated by Django 3.2.9 on 2021-11-13 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]
