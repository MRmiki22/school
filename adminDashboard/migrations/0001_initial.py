# Generated by Django 4.0.7 on 2023-08-17 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_name', models.CharField(help_text='Format: YYYY-YYYY (e.g., 2023-2024)', max_length=9, unique=True)),
            ],
            options={
                'verbose_name_plural': 'School Years',
            },
        ),
        migrations.CreateModel(
            name='School_Year_Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free', models.IntegerField()),
                ('schoolYear', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminDashboard.schoolyear')),
                ('student_in_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.class_student')),
            ],
        ),
    ]