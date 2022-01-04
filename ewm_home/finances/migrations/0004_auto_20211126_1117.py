# Generated by Django 3.2.9 on 2021-11-26 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0003_searches'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BankData',
            new_name='BankEntry',
        ),
        migrations.AlterModelOptions(
            name='bankentry',
            options={'verbose_name': 'Bank Entry'},
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='financetype',
            options={'verbose_name': 'Finance Type'},
        ),
        migrations.AlterModelOptions(
            name='searches',
            options={'verbose_name': 'Searches'},
        ),
    ]
