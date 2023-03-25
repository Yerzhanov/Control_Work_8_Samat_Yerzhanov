# Generated by Django 4.1.7 on 2023-03-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]