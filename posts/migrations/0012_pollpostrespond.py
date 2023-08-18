# Generated by Django 4.2.3 on 2023-08-17 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0011_postlike'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollPostRespond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.pollpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
