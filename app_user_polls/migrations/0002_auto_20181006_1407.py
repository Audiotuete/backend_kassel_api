# Generated by Django 2.0.8 on 2018-10-06 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_user_polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpoll',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_polls.Poll'),
        ),
    ]
