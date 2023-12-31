# Generated by Django 4.2.3 on 2023-07-23 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_rename_badge_desc_badges_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='badges',
            field=models.ManyToManyField(blank=True, to='accounts.badges'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='hub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.hub'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=models.ManyToManyField(blank=True, to='accounts.skill'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='social_media',
            field=models.ManyToManyField(blank=True, to='accounts.socialmedia'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
