# Generated by Django 4.1.11 on 2023-11-05 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productchart',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 5, 13, 55, 41, 786137)),
        ),
    ]
