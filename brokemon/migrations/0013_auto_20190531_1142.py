# Generated by Django 2.2.1 on 2019-05-31 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokemon', '0012_bmonblog_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmonblog',
            name='title_eight',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='title_five',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='title_four',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='title_intro',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='title_nine',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='title_one',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='title_seven',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='title_six',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='title_ten',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='title_three',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='title_two',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='bmonblog',
            name='intro',
            field=models.TextField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='bmonblog',
            name='par_one',
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]
