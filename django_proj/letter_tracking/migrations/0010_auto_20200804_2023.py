# Generated by Django 3.0.7 on 2020-08-04 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0009_auto_20200731_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='MX_mentioned',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'No')], default='null', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letter',
            name='action',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letter',
            name='author',
            field=models.CharField(default='defauly author', help_text='Names are displayed in <em>Last Name, First Name</em> format', max_length=60, verbose_name='Author Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letter',
            name='comments',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letter',
            name='cosigners',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letter',
            name='kind_of_statement',
            field=models.CharField(choices=[('Carta', 'Carta'), ('Consulta', 'Consulta'), ('Declaración', 'Declaracion')], default='defauly', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letter',
            name='kind_statement_party',
            field=models.CharField(choices=[('Carta', 'Carta'), ('Consulta', 'Consulta'), ('Declaración', 'Declaracion')], default='default', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letter',
            name='notice_num',
            field=models.CharField(default='default', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letter',
            name='positive_MX',
            field=models.CharField(choices=[('1', 'Positive'), ('2', 'Neurtal'), ('3', 'Negative')], default='default', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letter',
            name='recipient',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letter',
            name='specific_topic',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='letter',
            name='chamber',
            field=models.CharField(choices=[('B', 'Bicameral'), ('S', 'Senado'), ('C', 'Congreso')], max_length=9, verbose_name="Letter's Chamber of Origin"),
        ),
        migrations.AlterField(
            model_name='letter',
            name='description',
            field=models.TextField(verbose_name='Letter Description'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='legislator',
            field=models.CharField(help_text='Names are displayed in <em>Last Name, First Name</em> format', max_length=60, verbose_name='Legislator Name'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='link',
            field=models.URLField(verbose_name='Letter URL'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='rep_or_sen',
            field=models.CharField(choices=[('Rep.', 'Representative'), ('Sen.', 'Senator')], max_length=4, verbose_name='Representative or Senator'),
        ),
    ]
