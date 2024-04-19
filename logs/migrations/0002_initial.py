# Generated by Django 5.0.4 on 2024-04-19 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logs', '0001_initial'),
        ('podcast', '0001_initial'),
        ('userzone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewedchannel',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userzone.channel'),
        ),
        migrations.AddField(
            model_name='viewedchannel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userzone.user'),
        ),
        migrations.AddField(
            model_name='viewedcontent',
            name='episode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='podcast.episode'),
        ),
        migrations.AddField(
            model_name='viewedcontent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userzone.user'),
        ),
    ]