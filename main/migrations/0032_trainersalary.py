# Generated by Django 4.2.6 on 2023-10-31 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_trainer_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainerSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amt', models.IntegerField()),
                ('amt_date', models.DateField()),
                ('remarks', models.TextField(blank=True)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.trainer')),
            ],
            options={
                'verbose_name_plural': 'Trainer Salary',
            },
        ),
    ]
