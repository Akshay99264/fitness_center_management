# Generated by Django 4.2.6 on 2023-11-08 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_rename_f_name_queries_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='detail',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='title',
            new_name='label',
        ),
    ]
