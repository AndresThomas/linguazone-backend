# Generated by Django 3.2.4 on 2021-08-14 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0003_language_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='link',
            field=models.CharField(default='ww', max_length=30),
            preserve_default=False,
        ),
    ]
