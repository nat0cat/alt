# Generated by Django 4.2.5 on 2024-03-11 23:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import testapi.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessments',
            fields=[
                ('assessment_id', models.AutoField(primary_key=True, serialize=False)),
                ('assessment_title', models.CharField(max_length=100)),
                ('scale', models.IntegerField(validators=[testapi.models.MinValueValidator])),
                ('num_questions', models.IntegerField(validators=[testapi.models.MinValueValidator])),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=500)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapi.assessments')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('age', models.IntegerField(validators=[testapi.models.MinValueValidator])),
                ('gender', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='UserStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(validators=[testapi.models.MinValueValidator])),
                ('count', models.IntegerField(default=0, validators=[testapi.models.MinValueValidator])),
                ('num_questions', models.IntegerField(validators=[testapi.models.MinValueValidator])),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapi.assessments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapi.users')),
            ],
            options={
                'unique_together': {('user', 'assessment', 'count')},
            },
        ),
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=0, validators=[testapi.models.MinValueValidator])),
                ('count', models.IntegerField(default=0, validators=[testapi.models.MinValueValidator])),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapi.questions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapi.users')),
            ],
            options={
                'unique_together': {('user', 'question', 'count')},
            },
        ),
    ]
