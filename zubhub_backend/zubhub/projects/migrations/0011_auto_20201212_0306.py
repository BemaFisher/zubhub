# Generated by Django 2.2.7 on 2020-12-12 03:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20201210_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]