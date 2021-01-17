# Generated by Django 3.1.4 on 2021-01-08 21:07

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to=job.models.image_upload),
            preserve_default=False,
        ),
    ]
