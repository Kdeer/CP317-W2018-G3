# Generated by Django 2.0.6 on 2018-07-11 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subby', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
