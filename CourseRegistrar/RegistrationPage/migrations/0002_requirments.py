# Generated by Django 3.1.1 on 2020-10-31 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cs1', models.CharField(max_length=20)),
                ('cs2', models.CharField(max_length=20)),
                ('cs3', models.CharField(max_length=20)),
                ('cs4', models.CharField(max_length=20)),
                ('pr1', models.CharField(max_length=20)),
                ('pr2', models.CharField(max_length=20)),
                ('pr3', models.CharField(max_length=20)),
                ('pr4', models.CharField(max_length=20)),
                ('pr5', models.CharField(max_length=20)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RegistrationPage.course')),
            ],
        ),
    ]