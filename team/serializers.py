from rest_framework import serializers
# from project.serializers import ProjectViewSerializer
from .models import Team

class TeamViewSerializer(serializers.ModelSerializer):
    # project = ProjectViewSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = '__all__'