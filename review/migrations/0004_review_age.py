# Generated by Django 4.0.3 on 2022-09-09 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_review_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='age',
            field=models.PositiveIntegerField(default=1, help_text='User Age'),
            preserve_default=False,
        ),
    ]
