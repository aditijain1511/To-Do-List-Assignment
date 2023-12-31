# Generated by Django 3.2.20 on 2023-07-16 10:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('toDo_list', '0006_alter_todo_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='date',
        ),
        migrations.AddField(
            model_name='todo',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='todo',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
