from django.db import models
from project.models import Project
import uuid

# Create your models here.
class Eval(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name="linkId")
    isLocked = models.BooleanField(default=False)