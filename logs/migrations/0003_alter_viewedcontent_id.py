# Generated by Django 5.0.4 on 2024-04-19 13:49

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewedcontent',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9cad476f-1bed-4c13-936d-5eff1cd69be3'), editable=False, primary_key=True, serialize=False),
        ),
    ]
