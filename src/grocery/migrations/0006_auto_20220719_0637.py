# Generated by Django 2.1.5 on 2022-07-19 12:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0005_auto_20220718_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='last_updated',
            field=models.DateField(default=datetime.datetime(2022, 7, 19, 12, 37, 11, 427755, tzinfo=utc)),
        ),
    ]
