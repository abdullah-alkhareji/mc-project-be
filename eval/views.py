from rest_framework.viewsets import ModelViewSet
from .serializers import EvalSerializer
from .models import Eval

# Create your views here.
class EvalView(ModelViewSet):
    queryset = Eval.objects.all()
    serializer_class = EvalSerializer
