# Generated by Django 2.1.5 on 2020-06-30 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_auto_20200629_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='byindians',
            name='type',
            field=models.CharField(default='', max_length=300),
        ),
    ]
