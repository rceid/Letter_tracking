# Generated by Django 3.1 on 2020-08-25 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0053_auto_20200825_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='other_destinatario_comments',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='letter',
            name='destinatario',
            field=models.ManyToManyField(blank=True, help_text="<em>If 'Other', write notes in text box below</em>", to='letter_tracking.Recipient'),
        ),
    ]
