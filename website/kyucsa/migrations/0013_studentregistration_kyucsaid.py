# Generated by Django 4.2.2 on 2023-11-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyucsa', '0012_alter_studentregistration_academicstatus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentregistration',
            name='kyucsaId',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
