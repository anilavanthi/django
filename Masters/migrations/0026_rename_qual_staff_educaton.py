# Generated by Django 4.0.4 on 2023-06-01 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Masters', '0025_alter_staff_qual_alter_staff_source'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='qual',
            new_name='educaton',
        ),
    ]
