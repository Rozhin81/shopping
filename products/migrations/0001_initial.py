# Generated by Django 4.1.11 on 2023-10-19 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subcategory', '0001_initial'),
        ('seller', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('maker', models.CharField(max_length=50)),
                ('built_in', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('stars', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('seller_id', models.ManyToManyField(to='seller.seller')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subcategory.subcategory')),
            ],
        ),
    ]
