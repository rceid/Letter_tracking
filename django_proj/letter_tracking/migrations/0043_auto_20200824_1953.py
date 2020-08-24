# Generated by Django 3.1 on 2020-08-24 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0042_auto_20200824_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='legislator',
            old_name='test',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='legislator',
            name='district',
            field=models.CharField(choices=[('N/a', ''), ('at large', 'at large'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53')], default='def', help_text='If politician is a Sentor, please select N/a', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='legislator',
            name='first_name',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
