# Generated by Django 2.0.8 on 2018-10-05 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_questions', '0007_auto_20181005_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='poll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_polls.Poll'),
        ),
    ]