# Generated by Django 3.0.7 on 2020-07-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0003_letter_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='title',
        ),
        migrations.AddField(
            model_name='letter',
            name='code',
            field=models.CharField(default='', max_length=15),
        ),
    ]
