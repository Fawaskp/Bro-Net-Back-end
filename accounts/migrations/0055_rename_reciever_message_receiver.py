# Generated by Django 4.2.3 on 2023-08-20 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0054_message_reciever_alter_message_sender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='reciever',
            new_name='receiver',
        ),
    ]
