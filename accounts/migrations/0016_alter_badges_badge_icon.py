# Generated by Django 4.2.3 on 2023-07-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_stack_alter_badges_badge_icon_userprofile_stack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badges',
            name='badge_icon',
            field=models.ImageField(null=True, upload_to='badge-icons'),
        ),
    ]
