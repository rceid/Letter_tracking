# Generated by Django 3.1 on 2020-08-23 22:47

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0039_auto_20200823_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='cosigners',
        ),
        migrations.AddField(
            model_name='letter',
            name='cosigners',
            field=multiselectfield.db.fields.MultiSelectField(choices=[], default='None', max_length=200, verbose_name='Copatrocinador/a'),
        ),
    ]