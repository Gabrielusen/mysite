from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.title
