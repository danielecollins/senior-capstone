# Generated by Django 2.1.5 on 2022-07-14 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='last_modified',
            new_name='last_updated',
        ),
    ]