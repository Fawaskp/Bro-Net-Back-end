# Generated by Django 4.2.3 on 2023-08-06 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0042_usereducation_course_alter_skill_icon_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['id'], 'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='socialmedia',
            options={'ordering': ['id'], 'verbose_name_plural': 'Socila Media'},
        ),
        migrations.AlterModelOptions(
            name='usereducation',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.educationcategory'),
        ),
    ]
