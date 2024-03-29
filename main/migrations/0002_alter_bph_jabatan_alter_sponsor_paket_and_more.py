# Generated by Django 5.0.2 on 2024-03-01 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bph',
            name='jabatan',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='paket',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterUniqueTogether(
            name='sponsor',
            unique_together={('acara', 'perusahaan')},
        ),
    ]
