from dataclasses import fields
from rest_framework import serializers
from .models import Judge

class JudgeCreateSerializer(serializers.ModelSerializer):
    grade = serializers.ReadOnlyField()
    class Meta:
        model= Judge
        fields= "__all__"


    def create(self, validated_data):
        defaultCriteria = []
        for criteria in validated_data['eval'].project.criteria.all():
            defaultCriteria.append({"name": criteria.name, "weight": criteria.weight, "grade": 0})
        teams = []
        for team in validated_data['eval'].project.team.all():
            teams.append({"teamId": team.id, "teamName": team.name, "grade": defaultCriteria})
        validated_data['grade'] = teams
        return super().create(validated_data)

class JudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = "__all__"
