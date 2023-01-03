# Generated by Django 4.1.4 on 2022-12-29 06:33

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_rename_sitesettings_sitesetting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesetting',
            name='site_hero',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='site_logo',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='small_2',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='text_small_hero',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='text_title_hero',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='title_2',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='use_settings',
        ),
        migrations.CreateModel(
            name='SiteSettingTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('use_settings', models.BooleanField(default=False)),
                ('site_logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('site_hero', models.ImageField(blank=True, null=True, upload_to='')),
                ('text_title_hero', models.TextField(blank=True, null=True)),
                ('text_small_hero', models.TextField(blank=True, null=True)),
                ('title_2', models.TextField(blank=True, null=True)),
                ('small_2', models.TextField(blank=True, null=True)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='settings.sitesetting')),
            ],
            options={
                'verbose_name': 'site setting Translation',
                'db_table': 'settings_sitesetting_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases = (parler.models.TranslatableModel, models.Model),
        ),
    ]