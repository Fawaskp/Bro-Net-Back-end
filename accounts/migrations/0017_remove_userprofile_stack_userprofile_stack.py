# Generated by Django 4.2.3 on 2023-07-17 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_badges_badge_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='stack',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='stack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.stack'),
        ),
    ]
