# Generated by Django 4.1 on 2022-08-12 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('party', models.CharField(max_length=100)),
                ('votes', models.IntegerField(null=True)),
                ('votes_percentage', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=100)),
                ('constituency', models.CharField(max_length=100, unique=True)),
                ('registered_voters', models.IntegerField()),
                ('valid_votes', models.IntegerField()),
                ('spoilt_votes', models.IntegerField()),
                ('voter_turnout', models.IntegerField()),
            ],
        ),
    ]