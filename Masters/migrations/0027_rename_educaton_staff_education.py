# Generated by Django 4.0.4 on 2023-06-01 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Masters', '0026_rename_qual_staff_educaton'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='educaton',
            new_name='education',
        ),
    ]