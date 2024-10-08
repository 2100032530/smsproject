# Generated by Django 5.0.6 on 2024-06-07 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_alter_course_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.CharField(choices=[('CSE(Regular)', 'CSE(R)'), ('CSE(HONORS)', 'CSE(H)'), ('CS&IT', 'CSIT')], max_length=100),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='designation',
            field=models.CharField(choices=[('Professor', 'Professor'), ('AssistantProfessor', 'AssistantProfessor')], max_length=100),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Others', 'Others')], max_length=20),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='qualification',
            field=models.CharField(choices=[('B.TECH', 'B.TECH'), ('M.TECH', 'M.TECH'), ('Ph.D', 'Ph.D')], max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='Program',
            field=models.CharField(choices=[('B.TECH', 'B.TECH'), ('M.TECH', 'M.TECH')], max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('CSE(Regular)', 'CSE(R)'), ('CSE(HONORS)', 'CSE(H)'), ('CS&IT', 'CSIT')], max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Others', 'Others')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.CharField(choices=[('ODD', 'ODD'), ('EVEN', 'EVEN')], max_length=10),
        ),
    ]
