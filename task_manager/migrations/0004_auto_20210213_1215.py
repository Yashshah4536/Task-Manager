# Generated by Django 3.1.6 on 2021-02-13 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0003_auto_20210213_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('T', 'To Do'), ('D', 'Doing'), ('I', 'In Test'), ('O', 'Done'), ('B', 'Blocked'), ('L', 'Deleted')], max_length=1),
        ),
    ]
