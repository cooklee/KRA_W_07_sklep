# Generated by Django 3.1.6 on 2021-02-14 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modliszka', '0004_auto_20210214_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='products',
            field=models.ManyToManyField(through='modliszka.CarProduct', to='modliszka.Product'),
        ),
    ]