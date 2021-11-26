# Generated by Django 3.2.4 on 2021-11-06 21:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.CharField(db_index=True, max_length=100)),
                ('account', models.CharField(db_index=True, max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('amount', models.DecimalField(db_index=True, decimal_places=2, max_digits=6)),
                ('check_num', models.IntegerField(db_index=True)),
                ('has_cleared', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(db_index=True, default=datetime.datetime.now)),
                ('bank_date', models.DateField(db_index=True)),
                ('year', models.CharField(max_length=4)),
                ('month', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
    ]
