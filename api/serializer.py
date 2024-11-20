from rest_framework import serializers
from .models import Alumno, Rol, AlumnoRol, Profesor, Asignatura, Notas

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

# Serializador para el modelo AlumnoRol (relación entre Alumno y Rol)
class AlumnoRolSerializer(serializers.ModelSerializer):
    alumno = AlumnoSerializer()
    rol = RolSerializer()

    class Meta:
        model = AlumnoRol
        fields = ['alumno', 'rol', 'fecha_asignacion']

# Serializador para el modelo Profesor
class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'

# Serializador para el modelo Asignatura
class AsignaturaSerializer(serializers.ModelSerializer):
    profesor = ProfesorSerializer(read_only=True)  # Obtiene la información del Profesor relacionado

    class Meta:
        model = Asignatura
        fields = '__all__'

class NotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notas
        fields = '__all__'