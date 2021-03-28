# Generated by Django 3.0.7 on 2021-03-22 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_recruiter_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('salary', models.FloatField(max_length=20)),
                ('image', models.FileField(upload_to='')),
                ('description', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('skills', models.CharField(max_length=50)),
                ('creationdate', models.DateField(max_length=100)),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Recruiter')),
            ],
        ),
    ]
