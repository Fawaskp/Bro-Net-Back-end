# Generated by Django 4.2.3 on 2023-07-23 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_alter_project_options_alter_socialmedia_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
