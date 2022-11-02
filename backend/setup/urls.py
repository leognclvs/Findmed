from urllib import request
from django.contrib import admin
from django.urls import path, include
from findmed.views import SintomaViewSet, MedicamentoViewSet, IndicacaoViewSet, ListaSintomaMedicamento, teste
from rest_framework import routers

router = routers.DefaultRouter()
router.register('sintomas', SintomaViewSet, basename='Sintoma')
router.register('medicamentos', MedicamentoViewSet, basename='Medicamento')
router.register('indicacoes', IndicacaoViewSet, basename='Indicacao')
router.register('teste', teste, basename='teste')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('sintomas/<int:pk>/medicamentos/', ListaSintomaMedicamento.as_view(), name='ListaSintomaMedicamento'),
]
