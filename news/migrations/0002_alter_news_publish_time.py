# Generated by Django 4.1.4 on 2024-10-22 00:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
