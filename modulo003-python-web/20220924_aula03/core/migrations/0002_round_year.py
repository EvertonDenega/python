# Generated by Django 4.1.1 on 2022-09-24 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]