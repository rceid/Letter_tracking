# Generated by Django 3.1 on 2020-08-18 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0026_auto_20200817_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='acción',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='letter_tracking.action'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='caucus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='letter_tracking.caucus'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='destinatario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='letter_tracking.recipient'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='legislatura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='letter_tracking.legislature'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='tema',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='letter_tracking.topic'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='tema_específico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='letter_tracking.specific_topic'),
        ),
    ]