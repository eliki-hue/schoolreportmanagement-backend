# Generated by Django 3.2.1 on 2023-03-29 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default='email@mtkenyaacademy.ac.ke', max_length=255),
            preserve_default=False,
        ),
    ]
