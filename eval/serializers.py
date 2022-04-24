from dataclasses import field
from rest_framework import serializers
from judge.serializers import JudgeSerializer
from .models import Eval

class EvalSerializer(serializers.ModelSerializer):
    judge = JudgeSerializer(many=True, read_only=True)
    class Meta:
        model= Eval
        fields = "__all__"