from rest_framework import viewsets
from rest_framework.decorators import action

from ..serializer import AsignaturaSerializer
from ..models import Asignatura, CustomPageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class AsignaturasViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    @action(detail=False, methods=['delete'])
    def delete_all_teachers(self,request):
        Asignatura.objects.all().delete()
        return Response({"message": "Todos las asignaturas han sido eliminados correctamente."}, status=status.HTTP_204_NO_CONTENT)
