# Generated by Django 4.0.6 on 2022-09-14 11:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0002_alter_kategorimodel_options_yazilar'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Yazilar',
            new_name='YazilarlarModel',
        ),
    ]