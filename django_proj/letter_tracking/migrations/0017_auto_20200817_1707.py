# Generated by Django 3.1 on 2020-08-17 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0016_auto_20200817_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letter',
            old_name='recipient',
            new_name='destinatario',
        ),
        migrations.RenameField(
            model_name='letter',
            old_name='MX_mentioned',
            new_name='mención_directa_a_MX',
        ),
    ]
