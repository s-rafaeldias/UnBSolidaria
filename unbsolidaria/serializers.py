from .models import User, Trabalho
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'email', 'telefone')

class TrabalhoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trabalho
        fields = ('id', 'titulo', 'descricao', 'data_inicio', 'data_fim', 'vagas', 'dias', 'organizacao')
