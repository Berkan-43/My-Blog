# Generated by Django 4.0.6 on 2022-09-15 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_i̇letisimmodel_olusturulma_tarihi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yorummodel',
            old_name='guncellenme_tarihi',
            new_name='duzenlenme_tarihi',
        ),
    ]
