# Generated by Django 3.0 on 2020-04-12 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20200411_1820'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Client',
        ),
    ]
