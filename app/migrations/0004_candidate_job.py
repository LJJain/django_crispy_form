# Generated by Django 4.1.3 on 2022-11-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_candidate_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='job',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
