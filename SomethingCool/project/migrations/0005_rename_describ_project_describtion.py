# Generated by Django 4.0.6 on 2022-08-28 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_rename_description_project_describ'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='describ',
            new_name='describtion',
        ),
    ]