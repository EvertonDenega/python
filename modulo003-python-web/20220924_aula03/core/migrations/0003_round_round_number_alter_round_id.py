# Generated by Django 4.1.1 on 2022-09-24 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_round_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='round_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='round',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
