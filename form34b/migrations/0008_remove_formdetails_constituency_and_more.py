# Generated by Django 4.1 on 2022-08-16 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form34b', '0007_formdetails_mweure_formdetails_odinga_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formdetails',
            name='constituency',
        ),
        migrations.AlterField(
            model_name='formdetails',
            name='county',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
