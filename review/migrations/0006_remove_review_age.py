# Generated by Django 4.0.3 on 2022-09-09 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_alter_review_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='age',
        ),
    ]
