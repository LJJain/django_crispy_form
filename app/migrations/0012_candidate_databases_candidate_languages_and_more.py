# Generated by Django 4.1.3 on 2022-11-13 02:20

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_candidate_frameworks_alter_candidate_personality'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='databases',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('MySQL', 'MySQL'), ('Postgree', 'Postgree'), ('MongoDB', 'MongoDB'), ('SqLite3', 'SqLite3'), ('Oracle', 'Oracle'), ('Others', 'Others')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='candidate',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Python', 'Python'), ('Java', 'Java'), ('Javascript', 'Javascript'), ('C++', 'C++'), ('Ruby', 'Ruby'), ('Others', 'Others')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='candidate',
            name='libraries',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Ajax', 'Ajax'), ('Jquery', 'Jquery'), ('React.js', 'React.js'), ('Chart.js', 'Chart.js'), ('Gsap', 'Gsap'), ('Others', 'Others')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='candidate',
            name='mobile',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('React native', 'React native'), ('Kivy', 'Kivy'), ('Flutter', 'Flutter'), ('Ionic', 'Ionic'), ('Xamarim', 'Xamarim'), ('Others', 'Others')], default='', max_length=50),
        ),
        migrations.AddField(
            model_name='candidate',
            name='others',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('UML', 'UML'), ('SQL', 'SQL'), ('Docker', 'Docker'), ('GIT', 'GIT'), ('GraphQL', 'GraphQL'), ('Others', 'Others')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='frameworks',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Laravel', 'Laravel'), ('Angular', 'Angular'), ('Dango', 'Dango'), ('Flask', 'Flask'), ('Vue', 'Vue'), ('Others', 'Others')], default='', max_length=50),
        ),
    ]
