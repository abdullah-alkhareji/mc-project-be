import imp
from django.db import models
from eval.models import Eval

# Create your models here.
class Judge(models.Model):
    name = models.CharField(max_length=255)
    eval = models.ForeignKey(Eval, on_delete=models.CASCADE, related_name='judge')
    grade = models.JSONField(null=True, blank = True)
