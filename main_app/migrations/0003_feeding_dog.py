# Generated by Django 4.2.11 on 2024-04-09 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeding',
            name='dog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.dog'),
        ),
    ]
