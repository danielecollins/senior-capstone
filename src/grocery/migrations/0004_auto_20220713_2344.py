# Generated by Django 2.1.5 on 2022-07-14 05:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0003_auto_20220713_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='last_updated',
            field=models.DateField(default=datetime.datetime(2022, 7, 14, 5, 44, 30, 387456, tzinfo=utc)),
        ),
    ]