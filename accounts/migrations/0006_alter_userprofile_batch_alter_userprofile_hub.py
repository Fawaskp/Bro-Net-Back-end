# Generated by Django 4.2.3 on 2023-07-13 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='batch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.batch'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='hub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.hub'),
        ),
    ]
