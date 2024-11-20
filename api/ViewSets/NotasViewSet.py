from rest_framework import viewsets
from rest_framework.decorators import action

from ..serializer import NotasSerializer
from ..models import Notas, CustomPageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

#Como por defecto ya viene un crud de notas dejo este crud y añado yo uno para eliminar todos los profesores
class NotasViewSet(viewsets.ModelViewSet):
    queryset = Notas.objects.all()
    serializer_class = NotasSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination





