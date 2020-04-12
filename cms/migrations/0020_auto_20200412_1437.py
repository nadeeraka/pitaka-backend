# Generated by Django 3.0 on 2020-04-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0019_auto_20200412_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incometype',
            name='name',
            field=models.CharField(choices=[('S', 'Salary'), ('P', 'Property'), ('O', 'Other'), ('B', 'Business')], default='Bank', max_length=2),
        ),
    ]
