# Generated by Django 4.2.6 on 2023-11-01 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0034_notiftrainerstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainerMsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.trainer')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Messages For Trainer',
            },
        ),
    ]
