# Generated by Django 3.2.8 on 2022-11-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0013_rename_dislay_order_titles_display_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
