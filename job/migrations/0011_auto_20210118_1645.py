# Generated by Django 3.1.5 on 2021-01-18 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_apply_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='character',
            new_name='name',
        ),
    ]
