# Generated by Django 2.2.7 on 2021-04-18 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0036_auto_20210417_2327'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='category',
            name='projects_ca_search__4ee9e0_gin',
        ),
        migrations.RemoveField(
            model_name='category',
            name='search_vector',
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='projects.Category'),
        ),
    ]