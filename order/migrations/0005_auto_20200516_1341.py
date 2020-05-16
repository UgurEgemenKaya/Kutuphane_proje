# Generated by Django 3.0.3 on 2020-05-16 10:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20200510_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='adminnote',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Returned', 'Returned'), ('Canceled', 'Canceled')], default='New', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='teslim_tarih',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 31, 13, 41, 21, 173056)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('IadeEdildi', 'IadeEdildi'), ('Canceled', 'Canceled')], default='New', max_length=10),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='teslim_tarih',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 31, 13, 41, 21, 174055)),
        ),
    ]
