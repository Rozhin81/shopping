# Generated by Django 4.1.11 on 2023-10-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField(unique=True)),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('activation', models.BooleanField(default=False)),
                ('identifier_code', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 'seller',
            },
        ),
    ]