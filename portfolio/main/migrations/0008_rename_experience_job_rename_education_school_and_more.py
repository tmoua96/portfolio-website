# Generated by Django 5.0.6 on 2024-09-04 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_education_major_alter_education_degree'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Experience',
            new_name='Job',
        ),
        migrations.RenameModel(
            old_name='Education',
            new_name='School',
        ),
        migrations.AlterModelTable(
            name='job',
            table='main_experience',
        ),
        migrations.AlterModelTable(
            name='school',
            table='main_education',
        ),
    ]
