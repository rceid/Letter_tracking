# Generated by Django 3.0.7 on 2020-07-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0007_auto_20200730_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
