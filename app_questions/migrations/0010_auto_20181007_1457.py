# Generated by Django 2.0.8 on 2018-10-07 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_questions', '0009_auto_20181006_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_polls.Poll', verbose_name='Poll (not changeable after creation)'),
        ),
    ]
