from django.db import models
from django.contrib.auth.models import AbstractUser


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    demo = models.CharField(max_length=200, default='0000000')

    def __str__(self):
        return self.title
