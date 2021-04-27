# Generated by Django 3.1.4 on 2021-04-27 07:16

from datetime import datetime, timedelta

from django.db import migrations


def creating_one_record_in_each_database(apps, schema_editor):
    Student = apps.get_model("university", "Student")
    Teacher = apps.get_model("university", "Teacher")
    Homework = apps.get_model("university", "Homework")
    HomeworkResult = apps.get_model("university", "HomeworkResult")

    first_student = Student(first_name="Alex", last_name="Lukin")
    first_teacher = Teacher(first_name="Roman", last_name="Malginov")
    homework_lesson_1 = Homework(
        text="OOP_1", dl=timedelta(days=2) + datetime.now(), time_created=datetime.now()
    )
    result_1 = HomeworkResult(
        author=first_student,
        homework=homework_lesson_1,
        solution="123456789",
        time_created=datetime.now(),
    )

    first_student.save()
    first_teacher.save()
    homework_lesson_1.save()
    result_1.save()


class Migration(migrations.Migration):

    dependencies = [
        ("university", "0001_initial"),
    ]

    operations = [migrations.RunPython(creating_one_record_in_each_database)]
