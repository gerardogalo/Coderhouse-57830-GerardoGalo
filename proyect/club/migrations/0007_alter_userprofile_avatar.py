# Generated by Django 5.1 on 2024-09-30 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0006_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
