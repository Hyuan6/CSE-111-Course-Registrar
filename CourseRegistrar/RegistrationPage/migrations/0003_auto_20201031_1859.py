# Generated by Django 3.1.1 on 2020-11-01 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationPage', '0002_requirments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirments',
            name='cs1',
            field=models.CharField(max_length=20, verbose_name='Class Standing 1'),
        ),
    ]