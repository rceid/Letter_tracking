# Generated by Django 3.1 on 2020-09-08 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0083_auto_20200907_1902'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='letter',
            options={'ordering': ('fecha',)},
        ),
    ]