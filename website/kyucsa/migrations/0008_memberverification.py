# Generated by Django 4.2.2 on 2023-11-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyucsa', '0007_rename_program_student_programme_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='memberVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kyucsaId', models.CharField(max_length=8)),
            ],
        ),
    ]
