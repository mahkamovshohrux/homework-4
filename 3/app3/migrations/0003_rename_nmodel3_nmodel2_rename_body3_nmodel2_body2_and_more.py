# Generated by Django 4.2.5 on 2023-09-22 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0002_rename_nmodel2_nmodel3_rename_body2_nmodel3_body3_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nmodel3',
            new_name='Nmodel2',
        ),
        migrations.RenameField(
            model_name='nmodel2',
            old_name='body3',
            new_name='body2',
        ),
        migrations.RenameField(
            model_name='nmodel2',
            old_name='status3',
            new_name='status2',
        ),
        migrations.RenameField(
            model_name='nmodel2',
            old_name='title3',
            new_name='title2',
        ),
    ]