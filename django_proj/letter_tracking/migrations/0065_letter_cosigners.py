# Generated by Django 3.1 on 2020-08-31 17:35

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0064_auto_20200831_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='cosigners',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None'), ('None', 'None')], default='None', max_length=1000, verbose_name='Copatrocinador/a'),
        ),
    ]
