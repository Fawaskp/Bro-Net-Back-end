# Generated by Django 4.2.3 on 2023-08-07 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_donts_title_dos_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donts',
            old_name='donts',
            new_name='dont',
        ),
    ]
