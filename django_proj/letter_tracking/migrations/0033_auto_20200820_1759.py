# Generated by Django 3.1 on 2020-08-20 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0032_auto_20200820_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caucus',
            name='caucus_name',
            field=models.CharField(blank=True, default='Na', max_length=25, null=True),
        ),
    ]
