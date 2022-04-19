from rest_framework import serializers
from team.serializers import TeamViewSerializer
from .models import Project


class ProjectViewSerializer(serializers.ModelSerializer):
    team = TeamViewSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = '__all__'