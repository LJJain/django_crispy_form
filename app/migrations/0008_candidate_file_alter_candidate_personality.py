# Generated by Django 4.1.3 on 2022-11-12 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_gneder_candidate_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='personality',
            field=models.CharField(choices=[('I am Outgoing', 'I am Outgoing'), ('I am Sociable', 'I am Sociable'), ('I am Antisociable', 'I am Antisociable'), ('I am Discreet', 'I am Discreet'), ('I am Seriou', 'I am Seriou')], max_length=50, null=True),
        ),
    ]
