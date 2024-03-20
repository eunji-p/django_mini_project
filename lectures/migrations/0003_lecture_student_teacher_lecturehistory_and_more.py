# Generated by Django 4.2 on 2024-03-20 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0002_subject_delete_lecture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('introduction', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('signup_at', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('signup_at', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(max_length=100)),
                ('lecture_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LectureHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('finished_at', models.DateTimeField(auto_now_add=True)),
                ('test_score', models.FloatField()),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.lecture')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.student')),
            ],
        ),
        migrations.AddField(
            model_name='lecture',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectures.teacher'),
        ),
    ]