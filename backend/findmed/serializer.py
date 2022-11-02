from rest_framework import serializers
from .models import Sintoma, Medicamento, Indicacao

class SintomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sintoma
        fields = '__all__'

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class IndicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicacao
        fields = '__all__'

class ListaSintomaMedicamentoSerializer(serializers.ModelSerializer):
    medicamento = serializers.ReadOnlyField(source='medicamento.nome')
    dose = serializers.ReadOnlyField(source='medicamento.dose')
    concentracao = serializers.ReadOnlyField(source='medicamento.concentracao')
    posologia = serializers.ReadOnlyField(source='medicamento.posologia')
    class Meta:
        model = Indicacao
        fields = ['medicamento', 'dose', 'concentracao', 'posologia',]

