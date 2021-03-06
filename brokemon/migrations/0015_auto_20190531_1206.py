# Generated by Django 2.2.1 on 2019-05-31 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokemon', '0014_auto_20190531_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmonblog',
            name='intro',
            field=models.TextField(default='placeholder', max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='par_eight',
            field=models.TextField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='par_five',
            field=models.TextField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='par_four',
            field=models.TextField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='par_nine',
            field=models.TextField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='par_one',
            field=models.TextField(default='placeholder', max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='par_seven',
            field=models.TextField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='par_six',
            field=models.TextField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='par_ten',
            field=models.TextField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='par_three',
            field=models.TextField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='par_two',
            field=models.TextField(blank=True, max_length=10000),
        ),
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
    ]
