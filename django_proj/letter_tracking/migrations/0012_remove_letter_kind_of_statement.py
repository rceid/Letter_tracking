# Generated by Django 3.1 on 2020-08-17 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0011_auto_20200810_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='kind_of_statement',
        ),
    ]