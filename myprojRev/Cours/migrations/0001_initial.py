# Generated by Django 4.1 on 2024-12-15 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('titre', models.CharField(max_length=255)),
                ('categorie', models.CharField(choices=[('Mobile', 'Mobile'), ('BI', 'BI'), ('WEB', 'WEB')], max_length=20)),
            ],
        ),
    ]
