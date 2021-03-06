# Generated by Django 3.1 on 2020-09-08 01:06

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0085_auto_20200908_0021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='action',
            options={'ordering': ('action_name',)},
        ),
        migrations.AlterModelOptions(
            name='caucus',
            options={'ordering': ('caucus_name',), 'verbose_name_plural': 'Caucuses'},
        ),
        migrations.AlterModelOptions(
            name='legislature',
            options={'ordering': ('legislature_name',)},
        ),
        migrations.AlterModelOptions(
            name='recipient',
            options={'ordering': ('recipient_name',)},
        ),
        migrations.AlterModelOptions(
            name='specific_topic',
            options={'ordering': ('specific_topic_name',)},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ('topic_name',)},
        ),
        migrations.AlterField(
            model_name='letter',
            name='destinatario',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('N/a', 'N/a'), ('ACA', 'ACA'), ('BOP', 'BOP'), ('CBP', 'CBP'), ('CDC', 'CDC'), ('CRCL', 'CRCL'), ('DHS', 'DHS'), ('DOD', 'DOD'), ('DOE', 'DOE'), ('DOJ', 'DOJ'), ('DOL', 'DOL'), ('DOS', 'DOS'), ('DOT', 'DOT'), ('EMBAMEX', 'EMBAMEX'), ('EOIR', 'EOIR'), ('FEMA', 'FEMA'), ('GAO', 'GAO'), ('GEO', 'GEO'), ('HHS', 'HHS'), ('HUD', 'HUD'), ('House Appropiations Committee Leadership', 'House Appropiations Committee Leadership'), ('House Majority Leader', 'House Majority Leader'), ('House Minority Leader', 'House Minority Leader'), ('ICE', 'ICE'), ('IG DHS', 'IG DHS'), ('OJJDP', 'OJJDP'), ('POTUS', 'POTUS'), ('Senate Appropiations Committee Leadership', 'Senate Appropiations Committee Leadership'), ('Senate Majority Leader', 'Senate Majority Leader'), ('Senate Minority Leader', 'Senate Minority Leader'), ('USAID', 'USAID'), ('USBA', 'USBA'), ('USCIS', 'USCIS'), ('USTR', 'USTR'), ('VPOTUS', 'VPOTUS')], default='None', help_text="<em>If 'Other', please specify in the text box below</em>", max_length=100, verbose_name='Recipient(s)'),
        ),
    ]
