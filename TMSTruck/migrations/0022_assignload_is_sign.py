# Generated by Django 3.1 on 2020-08-31 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMSTruck', '0021_auto_20200831_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignload',
            name='is_sign',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
