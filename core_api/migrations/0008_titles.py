# Generated by Django 3.2.8 on 2022-09-01 08:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0007_sampletype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_created=True, default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=200)),
                ('disporder', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Titles',
                'verbose_name_plural': 'Titles',
                'db_table': 'Titles',
            },
        ),
    ]