# Generated by Django 3.1 on 2020-08-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0041_auto_20200824_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='cosigners',
        ),
        migrations.AddField(
            model_name='legislator',
            name='test',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]
