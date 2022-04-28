from rest_framework.viewsets import ModelViewSet
from .models import Judge
from .serializers import JudgeSerializer, JudgeCreateSerializer
# Create your views here.

class JudgeViewSet(ModelViewSet):
    queryset = Judge.objects.all()
    # serializer_class = JudgeSerializer

    def get_serializer_class(self):
        if(self.request.method == "POST"):
            return JudgeCreateSerializer
        return JudgeSerializer