from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("The name doesn't might has numeric values ")
        
        return nome

    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("The CPF might to has 11 digits")
        return cpf
    
    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError("The RG might to has 9 digits")

        return rg

    def validate_celular(self, celular):
        if len(celular) != 11:
            raise serializers.ValidationError("The cellphone might to has 11 digits")
        
        return celular
