# Generated by Django 4.2.3 on 2023-08-12 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0048_alter_usersocialmediaaccounts_social_media_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('following_user', 'followed_user')},
        ),
    ]
