from pyexpat import model
from django.forms import fields
from rest_framework import serializers
from .models import Project

class ProjectViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'