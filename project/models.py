from django.db import models
from criteria.models import Criteria
from semester.models import Semester

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255)
    weight = models.IntegerField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name="project")
    criteria = models.ManyToManyField(Criteria)

    def __str__(self):
        return self.name
