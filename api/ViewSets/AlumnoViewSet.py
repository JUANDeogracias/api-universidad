from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from api.models import Alumno, CustomPageNumberPagination, Asignatura
from ..serializer import AlumnoSerializer, AsignaturaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class AlumnoViewSet(ModelViewSet):
    queryset = Alumno.objects.all()

    serializer_class = AlumnoSerializer
    pagination_class = CustomPageNumberPagination

    @action(detail=False, methods=['get'])
    def getClienteById(self, request):
        alumno_id = request.query_params.get('id_alumno')

        if not alumno_id:
            return Response({"error": "Debe proporcionar un id_alumno."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            alumno_id = int(alumno_id)
        except ValueError:
            return Response({"error": "El id_alumno debe ser un número entero."}, status=status.HTTP_400_BAD_REQUEST)

        alumno = Alumno.objects.filter(id_alumno=alumno_id).first()

        if alumno is None:
            return Response({"error": "Alumno no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AlumnoSerializer(alumno)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def getAsignaturasPorAlumno(self, request):
        # Obtenemos el id del alumno desde los parámetros de la consulta
        alumno_id = request.query_params.get('id_alumno')

        # Comprobamos que se ha pasado un id
        if not alumno_id:
            return Response({"error": "El id_alumno es requerido."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            id_final = int(alumno_id)  # Convertimos el id a entero
        except ValueError:
            return Response({"error": "El id_alumno debe ser un número entero."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Obtenemos el alumno con el id proporcionado (un solo objeto)
            alumno = Alumno.objects.get(id_alumno=id_final)
        except Alumno.DoesNotExist:
            return Response({"error": "No se ha encontrado un alumno con el id proporcionado."},
                            status=status.HTTP_404_NOT_FOUND)

        # Obtenemos las asignaturas del alumno
        asignaturas_alumno = alumno.asignaturas.all()

        # Usamos el serializador para convertir las asignaturas a un formato adecuado para la respuesta
        serializer = AsignaturaSerializer(asignaturas_alumno, many=True)
        return Response(serializer.data)


