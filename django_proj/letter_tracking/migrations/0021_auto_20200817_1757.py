# Generated by Django 3.1 on 2020-08-17 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0020_auto_20200817_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='mención_directa_a_MX',
            field=models.IntegerField(choices=[('1', 'Yes'), ('0', 'No')], verbose_name='Was Mexico directly mentioned?'),
        ),
    ]
