# Generated by Django 4.2.6 on 2023-10-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_subplan_highlight_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='subplan',
            name='highlight_status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
