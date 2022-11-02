from rest_framework.decorators import action
from rest_framework import viewsets, generics, filters
from .models import Sintoma, Medicamento, Indicacao
from .serializer import SintomaSerializer, MedicamentoSerializer, IndicacaoSerializer, ListaSintomaMedicamentoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.db.models import Q
from django.db import connection

class SintomaViewSet(viewsets.ModelViewSet):
    queryset = Sintoma.objects.all()
    serializer_class = SintomaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

class IndicacaoViewSet(viewsets.ModelViewSet):
    queryset = Indicacao.objects.all()
    serializer_class = IndicacaoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['sintoma__id']

class ListaSintomaMedicamento(generics.ListAPIView):
    """Lista todos os medicamentos indicados para um sintoma"""
    def get_queryset(self):
       sintoma = self.kwargs['pk']
       return Indicacao.objects.filter(sintoma=sintoma)
    serializer_class = ListaSintomaMedicamentoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['medicamento__nome']

class teste(viewsets.ModelViewSet):
    queryset = Indicacao.objects.all()
    serializer_class = IndicacaoSerializer
    @action(detail=False, methods=['get'])
    def newest(self, request):
        list_id = request.data.getlist('list_id')
        list_nb = list(map(int, list_id))
        print(list_nb[0])
        and_condition = Q()
        for value in list_nb:
            and_condition.add(Q(**{'sintoma': value}), Q.OR)
        print(and_condition)
        
        query = Indicacao.objects.filter(and_condition).values('medicamento__nome', 'medicamento__dose','medicamento__concentracao', 'medicamento__posologia').distinct()
        print(query.query)

        return Response(query)

# def my_custom_sql():
#     with connection.cursor() as cursor:
#         cursor.execute("SE")
#         row = cursor.fetchone()

#     return row

# print(my_custom_sql())