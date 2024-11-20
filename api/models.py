from django.db import models
import enum
from rest_framework.pagination import PageNumberPagination

#definimos los tres tipos de rol que puede tener un usuario
class RolTipoEnum(enum.Enum):
    USER = "user"
    ADMIN = "admin"
    SUPERUSER = "superuser"

class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    email = models.EmailField(unique=True)

    asignaturas = models.ManyToManyField('Asignatura', related_name='alumnos', blank=True)

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)  # Use AutoField for auto-increment
    tipo_rol = models.CharField(
        max_length=50,
        choices=[(role.name, role.value) for role in RolTipoEnum],  # Defining available options
        default=RolTipoEnum.USER.value  # Default role is 'user'
    )

    def __str__(self):
        return self.tipo_rol

#Creamos la tabla que relaciona alumno y rol
class AlumnoRol(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.alumno.nombre} - {self.rol.tipo_rol}"


#Creamos la clase Profesores
class Profesor(models.Model):
    id_profesor = models.AutoField(primary_key=True)  # ID autoincremental
    nombre = models.CharField(max_length=100)  # Nombre del profesor
    email = models.EmailField(unique=True)  # Correo electrónico único
    especialidad = models.CharField(max_length=100, null=True, blank=True)  # Especialidad del profesor
    fecha_contratacion = models.DateTimeField(auto_now_add=True)  # Fecha en que se contrató al profesor

    def __str__(self):
        return self.nombre

#Creamos la clase Asignaturas

class Asignatura(models.Model):
    id_asignatura = models.AutoField(primary_key=True)  # ID autoincremental
    nombre = models.CharField(max_length=100)  # Nombre de la asignatura
    descripcion = models.TextField(null=True, blank=True)  # Breve descripción opcional
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha en que se creó la asignatura
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, related_name="asignaturas")
    #lo de related name especifica la relacion inversa

    def __str__(self):
        return self.nombre

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10 #Numero predeterminado de elementos por pagina
    page_size_query_param = 'page_size' #donde el cliente define el page_size
    max_page_size = 20
    page_query_param = 'page'


#La tabla intermedia entre alumno y asignatura es nota
class Notas(models.Model):
    id_alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        related_name="notas" #el related name será el nombre que aparecerá en la relacion inversa como foreign key
    )
    id_asignatura = models.ForeignKey(
        Asignatura,
        on_delete=models.CASCADE,
        related_name="notas"
    )
    trimestre = models.PositiveSmallIntegerField()
    calificacion = models.IntegerField()

    class Meta:
        unique_together = ('id_alumno', 'id_asignatura', 'trimestre')
