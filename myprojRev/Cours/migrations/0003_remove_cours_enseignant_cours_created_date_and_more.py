# Generated by Django 4.1 on 2024-12-15 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Cours', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cours',
            name='Enseignant',
        ),
        migrations.AddField(
            model_name='cours',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cours',
            name='date_publication',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cours',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='cours',
            name='code',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='cours',
            name='enseignant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cours', to=settings.AUTH_USER_MODEL),
        ),
    ]
