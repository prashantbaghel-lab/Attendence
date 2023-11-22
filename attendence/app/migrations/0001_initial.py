# Generated by Django 4.2.7 on 2023-11-21 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence_log',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Student_id', models.IntegerField()),
                ('course_id', models.IntegerField()),
                ('present', models.CharField(max_length=3)),
                ('submitted_by', models.CharField(max_length=100)),
                ('updated_at', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('department_id', models.IntegerField()),
                ('semester', models.CharField(max_length=5)),
                ('classs', models.CharField(max_length=5)),
                ('lecture_hours', models.CharField(max_length=5)),
                ('submitted_by', models.CharField(max_length=100)),
                ('updated_at', models.TimeField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.attendence_log')),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('submitted_by', models.CharField(max_length=100)),
                ('updated_at', models.TimeField()),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.courses')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_user', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('submitted_by', models.CharField(max_length=100)),
                ('updated_at', models.TimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.attendence_log')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('classs', models.CharField(max_length=100)),
                ('submitted_by', models.CharField(max_length=100)),
                ('updated_at', models.TimeField()),
                ('department_id', models.ManyToManyField(to='app.departments')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.attendence_log')),
            ],
        ),
    ]