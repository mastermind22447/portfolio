# Generated by Django 4.1.5 on 2023-01-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_projects_photo_projects_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='datascience',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='projects/photos'),
        ),
        migrations.AddField(
            model_name='datascience',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='projects/videos'),
        ),
        migrations.AddField(
            model_name='presentations',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='projects/photos'),
        ),
        migrations.AddField(
            model_name='presentations',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='projects/videos'),
        ),
    ]