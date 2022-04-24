from rest_framework import serializers
from team.serializers import TeamViewSerializer
from criteria.serializers import CriteriaViewSerializer
from eval.serializers import EvalSerializer
from .models import Project


class ProjectViewSerializer(serializers.ModelSerializer):
    team = TeamViewSerializer(many=True, read_only=True)
    criteria = CriteriaViewSerializer(many=True)
    linkId = EvalSerializer( read_only=True)
    class Meta:
        model = Project
        fields = '__all__'