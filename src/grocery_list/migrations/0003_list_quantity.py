# Generated by Django 2.1.5 on 2022-07-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0002_auto_20220719_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]