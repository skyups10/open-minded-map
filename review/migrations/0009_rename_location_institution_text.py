# Generated by Django 4.0.3 on 2022-09-13 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0008_institution_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institution',
            old_name='location',
            new_name='text',
        ),
    ]