# Generated by Django 4.2.3 on 2023-08-16 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]