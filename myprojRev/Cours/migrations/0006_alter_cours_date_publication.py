# Generated by Django 4.1 on 2024-12-15 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cours', '0005_alter_cours_date_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='date_publication',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 15, 14, 33, 15, 723274, tzinfo=datetime.timezone.utc)),
        ),
    ]
