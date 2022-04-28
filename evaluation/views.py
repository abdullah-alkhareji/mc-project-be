from rest_framework.viewsets import ModelViewSet
from .serializers import EvaSerializer
from .models import Evaluation

# Create your views here.
class EvaViewSet(ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaSerializer