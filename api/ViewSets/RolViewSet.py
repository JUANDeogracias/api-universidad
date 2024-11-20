import enum

from rest_framework import viewsets
from rest_framework.decorators import action

from ..serializer import AlumnoSerializer, RolSerializer,AlumnoRolSerializer
from ..models import Alumno, Rol, AlumnoRol, CustomPageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    @action(detail=False, methods=['get'])
    def getRolByIdAlumno(self, request):
        alumno_id = request.query_params.get('id_alumno')

        if not alumno_id:
            return Response({"error": "El campo id_alumno es requerido"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            alumno = Alumno.objects.get(id_alumno=alumno_id)
            alumno_roles = AlumnoRol.objects.filter(alumno=alumno)
            roles = [alumno_rol.rol for alumno_rol in alumno_roles]
            serializer = RolSerializer(roles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Alumno.DoesNotExist:
            return Response({"error": "Alumno no encontrado"}, status=status.HTTP_404_NOT_FOUND)
