from rest_framework import serializers
from ..models import PessoaBancoDeDados

class PessoaSerializer(ModelSerializer):
    class Meta:
        model = PessoaBancoDeDados