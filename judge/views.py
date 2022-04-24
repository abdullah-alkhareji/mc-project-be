from rest_framework.viewsets import ModelViewSet

from judge.models import Judge
from judge.serializers import JudgeCreateSerializer, JudgeSerializer

# Create your views here.
class JudgeView(ModelViewSet):
    queryset= Judge.objects.all()
    # serializer_class= JudgeSerializer

    def get_serializer_class(self):
        if(self.request.method == "POST"):
            return JudgeCreateSerializer
        return JudgeSerializer