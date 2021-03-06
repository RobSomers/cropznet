# Generated by Django 2.2.1 on 2019-05-24 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokemon', '0005_auto_20190522_1644'),
    ]

    operations = [
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
            name='pic_five',
            field=models.CharField(blank=True, max_length=115),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='pic_four',
            field=models.CharField(blank=True, max_length=115),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='pic_one',
            field=models.CharField(blank=True, max_length=115),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='pic_three',
            field=models.CharField(blank=True, max_length=115),
        ),
        migrations.AddField(
            model_name='bmonblog',
            name='pic_two',
            field=models.CharField(blank=True, max_length=115),
        ),
        migrations.AlterField(
            model_name='bmonblog',
            name='pokemon',
            field=models.CharField(blank=True, default='/static/brokemon/images/sprites/<django.db.models.fields.CharField>.png', max_length=100),
        ),
    ]
