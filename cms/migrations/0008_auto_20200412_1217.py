# Generated by Django 3.0 on 2020-04-12 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20200412_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incometype',
            old_name='type',
            new_name='name',
        ),
    ]
