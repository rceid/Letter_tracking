# Generated by Django 3.0.7 on 2020-07-30 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0002_auto_20200730_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='title',
            field=models.CharField(default='Default Title', max_length=25),
            preserve_default=False,
        ),
    ]
