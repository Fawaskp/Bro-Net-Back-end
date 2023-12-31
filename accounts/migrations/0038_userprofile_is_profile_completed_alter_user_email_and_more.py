# Generated by Django 4.2.3 on 2023-07-25 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_workexperience'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_profile_completed',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, db_index=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='fullname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_profile_completed',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.batch'),
        ),
    ]
