# Generated by Django 3.1 on 2020-08-26 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMSTruck', '0007_assignload_is_awaiting'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrier',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
