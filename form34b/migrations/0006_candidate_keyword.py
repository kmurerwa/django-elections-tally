# Generated by Django 4.1 on 2022-08-12 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form34b', '0005_alter_formdetails_voter_turnout'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='keyword',
            field=models.CharField(default='', max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
