# Generated by Django 3.2.4 on 2021-08-12 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='language',
            old_name='name',
            new_name='language',
        ),
    ]
