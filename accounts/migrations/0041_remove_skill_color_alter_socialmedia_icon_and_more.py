# Generated by Django 4.2.3 on 2023-07-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_alter_socialmedia_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='color',
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='icon',
            field=models.ImageField(blank=True, upload_to='social-media-icons'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='name',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
