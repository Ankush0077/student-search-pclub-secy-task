from django.db import models
from django.urls import reverse

class StudentTaskFive(models.Model):
    name = models.CharField(max_length=200)
    userid = models.CharField(max_length=200)
    roll_no = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student:student_edit', kwargs={'pk': self.pk})
