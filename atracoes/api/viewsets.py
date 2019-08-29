from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracoesSerializer

class AtracoesViewSet(modelViewSet):
    queryset = Atracao.object.all()
    serializer_class = AtracoesSerializer