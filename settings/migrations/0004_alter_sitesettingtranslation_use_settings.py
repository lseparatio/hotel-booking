# Generated by Django 4.1.4 on 2022-12-29 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_remove_sitesetting_site_hero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettingtranslation',
            name='use_settings',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
