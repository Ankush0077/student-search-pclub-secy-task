# Generated by Django 4.1 on 2022-08-16 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="student_guide",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="student.student"
            ),
        ),
    ]