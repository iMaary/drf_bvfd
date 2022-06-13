from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_is_valid(data['cpf']):
            raise serializers.ValidationError({'cpf': 'The CPF might to has 11 digits'})
        if not name_is_valid(data['nome']):
            raise serializers.ValidationError({'nome': 'The name not might has numeric values'})
        if not rg_is_valid(data['rg']):
            raise serializers.ValidationError({'rg': 'The RG might to has 9 digits'})
        if not cellphone_is_valid(data['celular']):
            raise serializers.ValidationError({'celular': 'The cellphone might to has 11 digits'})

        return data
