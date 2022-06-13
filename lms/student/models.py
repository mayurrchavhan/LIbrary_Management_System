from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.first_name, self.last_name)