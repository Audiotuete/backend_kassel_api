# Generated by Django 2.0.8 on 2019-01-02 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_user_polls', '0003_auto_20181006_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpoll',
            name='poll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_polls.Poll'),
        ),
    ]
