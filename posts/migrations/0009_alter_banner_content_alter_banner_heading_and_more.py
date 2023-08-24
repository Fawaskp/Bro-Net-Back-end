# Generated by Django 4.2.3 on 2023-08-16 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_banner_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='content',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='banner',
            name='heading',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='banner',
            name='status',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]