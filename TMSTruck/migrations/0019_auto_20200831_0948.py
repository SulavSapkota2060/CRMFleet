# Generated by Django 3.1 on 2020-08-31 04:03

import TMSTruck.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TMSTruck', '0018_assignload_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='userRole',
            field=models.CharField(choices=[('Trainee', 'Trainee'), ('Logistics Manager', 'Logistics Manager'), ('Accounting Manager', 'Accounting Manager'), ('Hiring Manager', 'Hiring Manager'), ('Admin', 'Admin')], default='Trainee', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='ndaNca',
            field=models.FileField(upload_to=TMSTruck.models.w9UploadFile),
        ),
        migrations.AlterField(
            model_name='account',
            name='w9_upload',
            field=models.FileField(null=True, upload_to=TMSTruck.models.w9UploadFile),
        ),
        migrations.AlterField(
            model_name='assignload',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TMSTruck.account'),
        ),
        migrations.AlterField(
            model_name='carrier',
            name='mc_upload',
            field=models.FileField(null=True, upload_to=TMSTruck.models.carrierMcFiles),
        ),
    ]
