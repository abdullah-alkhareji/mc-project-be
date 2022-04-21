from django.db import models
# from project.models import Project

# Create your models here.
class Criteria(models.Model):
    name = models.CharField(max_length=255)
    weight = models.IntegerField()


    def __str__(self):
        return self.name