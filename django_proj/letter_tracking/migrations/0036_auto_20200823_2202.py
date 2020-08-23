# Generated by Django 3.1 on 2020-08-23 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0035_auto_20200820_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='cosigners',
        ),
        migrations.AddField(
            model_name='letter',
            name='cosigners',
            field=models.ManyToManyField(blank=True, null=True, related_name='copatrocinador', to='letter_tracking.Legislator', verbose_name='Copatrocinador/a'),
        ),
    ]
