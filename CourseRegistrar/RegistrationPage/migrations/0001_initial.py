# Generated by Django 3.1.1 on 2020-12-10 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crn', models.IntegerField()),
                ('Instructor', models.CharField(max_length=30)),
                ('Title', models.CharField(max_length=20)),
                ('cnum', models.CharField(max_length=15, verbose_name='Course Number')),
                ('Actv', models.CharField(max_length=15, verbose_name='Type of class')),
                ('Units', models.IntegerField(default=0)),
                ('Days', models.CharField(max_length=10)),
                ('TimeOfLec', models.CharField(max_length=10)),
                ('Bldg_Rm', models.CharField(default='REMOTE ONLY', max_length=20)),
                ('Start', models.CharField(max_length=10)),
                ('End', models.CharField(max_length=10)),
                ('Max_enrl', models.IntegerField()),
                ('Act_enrl', models.IntegerField()),
                ('Seats_avil', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Requirments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=15)),
                ('cs1', models.CharField(max_length=20, verbose_name='Class Standing 1')),
                ('cs2', models.CharField(blank=True, max_length=20, null=True)),
                ('cs3', models.CharField(blank=True, max_length=20, null=True)),
                ('cs4', models.CharField(blank=True, max_length=20, null=True)),
                ('pr1', models.CharField(blank=True, max_length=20, null=True)),
                ('pr2', models.CharField(blank=True, max_length=20, null=True)),
                ('pr3', models.CharField(blank=True, max_length=20, null=True)),
                ('pr4', models.CharField(blank=True, max_length=20, null=True)),
                ('pr5', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=15)),
                ('student', models.IntegerField()),
                ('grade', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_ID', models.IntegerField(unique=True)),
                ('Password', models.CharField(max_length=20)),
                ('Username', models.CharField(max_length=20, unique=True)),
                ('Class_Standing', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], max_length=2)),
                ('Phone_Number', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
            ],
        ),
    ]