# Generated by Django 3.0.3 on 2020-05-10 16:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_orderproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='teslim_tarih',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 25, 19, 47, 47, 234351)),
        ),
    ]