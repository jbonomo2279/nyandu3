from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=30, help_text= "Nombre del país")

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Paises"


class Provincia(models.Model):
    nombre = models.CharField(max_length=30, help_text= "Nombre de la provincia")
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE , help_text="País al que pertenece la provincia")

    def __str__(self):
        return f" Provincia {self.nombre} de {self.pais.nombre} "

    class Meta:
        verbose_name_plural = "Provincias"



class Aeropuerto(models.Model):
    nombre = models.CharField(max_length=30, help_text= "Nombre del aeropuerto")
    codigo_iata = models.CharField(max_length=3, help_text= "Código IATA del aeropuerto")
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, help_text= "Provincia donde está el aeropuerto")

    def __str__(self):
        return f"{self.nombre} {self.codigo_iata}"

    class Meta:
        verbose_name_plural = "Aeropuertos"

class Fabricante(models.Model):
    nombre = models.CharField(max_length=30, help_text= "Nombre del proveedor de aviones")
    contacto = models.TextField(help_text= "Contacto del proveedor de aviones, puede ingresar el nombre del contacto telefono, email u otras redes sociales del mismo")

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Fabricantes"


class Modelo(models.Model):
    nombre = models.CharField(max_length=30, help_text= "Nombre del modelo de avión")
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, help_text= "Fabricante del modelo de avión")

    def __str__(self):
        return f"{self.nombre} de {self.fabricante.nombre}"

    class Meta:
        verbose_name_plural = "Modelos"

class Avion(models.Model):
    matricula = models.CharField(max_length=30, help_text= "Matricula del avión")
    capacidad = models.PositiveSmallIntegerField(help_text= "Capacidad de pasajeros del avión")
    autonomia = models.PositiveIntegerField(help_text= "Autonomía del avión volando en línea recta a velocidad crucero, se expresa en millas")
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, help_text= "Fabricante del modelo de avión")


    def __str__(self):
        return f"Matricula {self.matricula} Modelo {self.modelo.nombre}"

    class Meta:
        verbose_name_plural = "Aviones"


class Categoria(models.Model):
    nombre = models.CharField(max_length=30,help_text= "Nombre de la categoría")
    descripcion_categoria = models.TextField(help_text= "Descripción de la categoría")


    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "Categorias"

class Empleado(models.Model):
    GENERO = {
        "M":"Masculino",
        "F":"Femenino",
        "X": "Otro",
        }
    nombre_completo = models.CharField(max_length=60, help_text= "Nombre y Apellido del empleado")
    email = models.EmailField(max_length=254,help_text= "Correo electrónico del empleado")
    telefono = models.CharField(max_length=30,help_text= "Teléfono del empleado")
    direccion = models.CharField(max_length=30,help_text= "Dirección donde reside el empleado")
    localidad = models.CharField(max_length=30,help_text= "Localidad donde reside el empleado")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, help_text= "Categoria del empleado")
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, help_text= "Provincia donde reside el empleado")
    genero = models.CharField(max_length=1, choices=GENERO,help_text="Género con el que se autopersive el empleado.")


    def __str__(self):
        return f"{self.id} : {self.nombre_completo}"

    class Meta:
        verbose_name_plural = "Empleados"

class Vuelo(models.Model):
    fecha_vuelo = models.DateField(blank=True, null=True, help_text="Día en que comienza el vuelo")
    hora_vuelo = models.TimeField(blank=True, null=True, help_text="Hora en que despega el vuelo")
    origen = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE, help_text= "Aeropuerto donde sale el vuelo")
    destino = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE, help_text= "Aeropuerto donde llega el vuelo", related_name="+")
    avion_vuelo = models.ForeignKey(Avion, on_delete=models.CASCADE, help_text= "Avión que realiza el vuelo")


    def __str__(self):
        return f"{self.id} de {self.origen.codigo_iata} a {self.destino.codigo_iata} "

    class Meta:
        verbose_name_plural = "Vuelos"



