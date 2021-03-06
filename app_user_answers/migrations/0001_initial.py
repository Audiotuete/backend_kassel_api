# Generated by Django 2.0.8 on 2019-01-14 08:10

from django.conf import settings
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_questions', '0011_auto_20190114_0749'),
        ('app_polls', '0003_remove_poll_poll_creator'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswerMultiple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_touched', models.DateTimeField(blank=True, null=True)),
                ('last_touched', models.DateTimeField(auto_now=True)),
                ('count_touched', models.PositiveIntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('answer_choice_key', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True), default=list, null=True, size=6)),
                ('poll', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_polls.Poll')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_questions.QuestionMultiple')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserAnswerOpen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_touched', models.DateTimeField(blank=True, null=True)),
                ('last_touched', models.DateTimeField(auto_now=True)),
                ('count_touched', models.PositiveIntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('answer_text', models.TextField(blank=True, max_length=250, null=True)),
                ('poll', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_polls.Poll')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_questions.QuestionOpen')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserAnswerYesOrNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_touched', models.DateTimeField(blank=True, null=True)),
                ('last_touched', models.DateTimeField(auto_now=True)),
                ('count_touched', models.PositiveIntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('answer_value', models.IntegerField(default=-1, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(0)])),
                ('answer_note', models.TextField(blank=True, max_length=250, null=True)),
                ('poll', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_polls.Poll')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_questions.QuestionYesOrNo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='useransweryesorno',
            unique_together={('user', 'question')},
        ),
        migrations.AlterUniqueTogether(
            name='useransweropen',
            unique_together={('user', 'question')},
        ),
        migrations.AlterUniqueTogether(
            name='useranswermultiple',
            unique_together={('user', 'question')},
        ),
    ]
