# Generated by Django 4.2.19 on 2025-03-05 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naileditapi', '0006_alter_project_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='uid',
            field=models.CharField(max_length=30),
        ),
    ]
