# Generated by Django 4.1.4 on 2023-01-04 12:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0009_indexpagetranslation_first_of_4_subtitle_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indexpagetranslation',
            old_name='presemtation_description',
            new_name='presentation_description',
        ),
        migrations.AlterField(
            model_name='indexpagetranslation',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]
