# Generated by Django 3.1 on 2020-08-25 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TMSTruck', '0003_auto_20200825_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='userRole',
        ),
    ]
