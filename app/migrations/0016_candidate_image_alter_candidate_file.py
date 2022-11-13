# Generated by Django 4.1.3 on 2022-11-13 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_candidate_about_course_candidate_about_job_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='image',
            field=models.ImageField(blank=True, upload_to='photo', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='file',
            field=models.FileField(blank=True, upload_to='resume', verbose_name='Resume'),
        ),
    ]