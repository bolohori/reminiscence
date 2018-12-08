# Generated by Django 2.1.2 on 2018-12-08 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_auto_20181208_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='icon_url',
            field=models.CharField(max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='media_path',
            field=models.CharField(max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='subdir',
            field=models.CharField(max_length=8192, null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='summary',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='tags',
            field=models.CharField(max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='title',
            field=models.CharField(max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='library',
            name='url',
            field=models.CharField(max_length=4096, null=True),
        ),
    ]