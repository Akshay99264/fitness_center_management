# Generated by Django 4.2.6 on 2023-11-01 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_trainermsg_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainermsg',
            name='user_type',
        ),
    ]
