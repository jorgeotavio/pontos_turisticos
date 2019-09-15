from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from comentarios.api.serializers import ComentarioSerializer


class PontoTuristicoSerializer(ModelSerializer):
    comentarios = ComentarioSerializer(many=True)

    class Meta:
        model = PontoTuristico
        fields = (
            'id',
            'nome',
            'descricao',
            'aprovado',
            'foto',
            'atracoes',
            'comentarios',
            'avaliacoes',
            'endereco'
        )