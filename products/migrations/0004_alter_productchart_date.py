# Generated by Django 4.1.11 on 2023-11-05 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_productchart_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productchart',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 5, 14, 10, 57, 534310)),
        ),
    ]
