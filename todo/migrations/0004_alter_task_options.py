# Generated by Django 4.2.7 on 2023-11-08 16:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0003_alter_task_deadline"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ("is_done", "-created_at")},
        ),
    ]
