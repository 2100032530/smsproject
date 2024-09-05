# Generated by Django 5.0.6 on 2024-06-18 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0010_course_credits_course_ltps'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultycoursemapping',
            name='component',
            field=models.CharField(choices=[('L', 'Lecture'), ('T', 'Tutorial'), ('P', 'Practical'), ('S', 'Skilling')], default='L', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facultycoursemapping',
            name='section',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facultycoursemapping',
            name='type',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
