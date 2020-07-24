# Generated by Django 2.1.5 on 2020-06-28 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_delete_byindian'),
    ]

    operations = [
        migrations.CreateModel(
            name='byindian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=800)),
                ('views', models.IntegerField()),
                ('date_published', models.CharField(default='', max_length=20)),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('channelname', models.CharField(default='', max_length=500)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
    ]
