from rest_framework import viewsets
from rest_framework.decorators import action

from ..serializer import ProfesorSerializer
from ..models import Profesor, CustomPageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

#Como por defecto ya viene un crud de profesores dejo este crud y añado yo uno para eliminar todos los profesores
class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    @action(detail=False, methods=['delete'])
    def delete_all_teachers(self,request):
        Profesor.objects.all().delete() #Eliminacion de todos los profesores
        return Response({"message": "Todos los profesores han sido eliminados correctamente."}, status=status.HTTP_204_NO_CONTENT)
