# Generated by Django 4.1 on 2024-12-15 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cours', '0007_alter_cours_date_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='date_publication',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 15, 14, 45, 5, 408846, tzinfo=datetime.timezone.utc)),
        ),
    ]
