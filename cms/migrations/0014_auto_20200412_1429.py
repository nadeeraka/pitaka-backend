# Generated by Django 3.0 on 2020-04-12 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_auto_20200412_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incometype',
            name='name',
            field=models.CharField(choices=[('S', 'Salary'), ('P', 'Property'), ('B', 'Business'), ('O', 'Other')], default='Bank', max_length=2),
        ),
    ]
