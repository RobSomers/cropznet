# Generated by Django 2.2.1 on 2019-05-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokemon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmonblog',
            name='date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
