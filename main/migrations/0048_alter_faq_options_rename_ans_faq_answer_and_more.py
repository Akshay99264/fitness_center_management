# Generated by Django 4.2.6 on 2023-11-09 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_rename_detail_page_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name_plural': 'FAQ'},
        ),
        migrations.RenameField(
            model_name='faq',
            old_name='ans',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='faq',
            old_name='quest',
            new_name='question',
        ),
    ]
