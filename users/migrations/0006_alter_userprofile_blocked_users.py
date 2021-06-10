# Generated by Django 3.2 on 2021-06-10 09:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_userprofile_blocked_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='blocked_users',
            field=models.ManyToManyField(blank=True, related_name='blocked', to=settings.AUTH_USER_MODEL),
        ),
    ]