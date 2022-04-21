# Generated by Django 4.0.4 on 2022-04-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('criteria', '0002_criteria_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criteria',
            name='project',
        ),
        migrations.AddField(
            model_name='criteria',
            name='project',
            field=models.ManyToManyField(to='project.project'),
        ),
    ]
