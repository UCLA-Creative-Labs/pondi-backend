# Generated by Django 2.1.7 on 2019-02-19 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pondi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='animal',
            field=models.CharField(default='porcupine', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='color',
            field=models.CharField(default='olive', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
