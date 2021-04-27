from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Teacher(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)


class Homework(models.Model):
    text = models.CharField(max_length=250)
    dl = models.DateTimeField()
    time_created = models.DateTimeField()


class HomeworkResult(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.CharField(max_length=250)
    time_created = models.DateTimeField()
