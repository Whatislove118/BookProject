# Generated by Django 3.2.6 on 2021-08-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizzeria',
            old_name='name',
            new_name='pizzeria_name',
        ),
        migrations.AddField(
            model_name='pizzeria',
            name='city',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='pizzeria',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]