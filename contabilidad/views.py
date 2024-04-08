# En tu archivo views.py dentro de la app contabilidad_personal

from rest_framework import generics
from .models import Gasto
from .serializers import GastoSerializer
from datetime import datetime
from django.utils import timezone

class GastoListView(generics.ListAPIView):
    serializer_class = GastoSerializer

    def get_queryset(self):
        fecha = self.request.query_params.get('fecha', None)
        if fecha:
            return Gasto.objects.filter(fecha=fecha)
        else:
            today = timezone.now()
            return Gasto.objects.filter(fecha__year=today.year, fecha__month=today.month)


class GastoCreateView(generics.CreateAPIView):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer