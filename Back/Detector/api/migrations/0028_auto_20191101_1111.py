# Generated by Django 2.2.6 on 2019-11-01 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20191101_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eye',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='eye_brow',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='mouse',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='nose',
            old_name='name',
            new_name='title',
        ),
    ]
