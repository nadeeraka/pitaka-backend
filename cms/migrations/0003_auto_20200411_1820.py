# Generated by Django 3.0 on 2020-04-11 18:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20200411_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('note', models.CharField(max_length=100, unique=True)),
                ('amount', models.DecimalField(decimal_places=4, default=0, max_digits=100)),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('note', models.CharField(max_length=100, unique=True)),
                ('amount', models.DecimalField(decimal_places=4, default=0, max_digits=100)),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('note', models.CharField(max_length=100, unique=True)),
                ('amount', models.DecimalField(decimal_places=4, default=0, max_digits=100)),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('rate', models.DecimalField(decimal_places=4, default=0, max_digits=100)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SavingType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('saving', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Saving')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='saving',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='savings', to='cms.SavingType'),
        ),
        migrations.AddField(
            model_name='saving',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.User'),
        ),
        migrations.CreateModel(
            name='IncomeType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('income', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Income')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='income',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to='cms.IncomeType'),
        ),
        migrations.AddField(
            model_name='income',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.User'),
        ),
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Expense')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='expense',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='cms.ExpenseType'),
        ),
        migrations.AddField(
            model_name='expense',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.User'),
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100, unique=True)),
                ('amount', models.DecimalField(decimal_places=4, default=0, max_digits=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.User')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
