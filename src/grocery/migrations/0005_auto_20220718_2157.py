# Generated by Django 2.1.5 on 2022-07-19 03:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0004_auto_20220713_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='albertsons_price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='broulims_price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='last_updated',
            field=models.DateField(default=datetime.datetime(2022, 7, 19, 3, 57, 48, 832845, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='item',
            name='walmart_price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
