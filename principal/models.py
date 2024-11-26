from django.db import models

# Create your models here.

###################################################################################################
#                                    Sección Noticias
###################################################################################################    
    
###################################################################################################

from django.db import models

class Social(models.Model):
    imagen_social = models.ImageField(upload_to='social/', null=True, blank=True)  
    titulo_social = models.CharField(max_length=200)
    fecha_social = models.DateField()
    servicio = models.CharField(max_length=100)
    nombre_ciudad = models.CharField(max_length=100)
    nombre_tipo_servicio = models.CharField(max_length=100)
    texto_social = models.TextField()
    imagen1 = models.ImageField(upload_to='Imagenes1/', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='Imagenes1/', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='Imagenes1/', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='Imagenes1/', null=True, blank=True)

    def __str__(self):
        return self.titulo_social

class Social_imagen1(models.Model):
    social = models.ForeignKey(Social, on_delete=models.CASCADE, related_name='imagenes1')
    imagen = models.ImageField(upload_to='Imagenes1/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Social_imagen2(models.Model):
    social = models.ForeignKey(Social, on_delete=models.CASCADE, related_name='imagenes2')
    imagen = models.ImageField(upload_to='Imagenes1/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Social_imagen3(models.Model):
    social = models.ForeignKey(Social, on_delete=models.CASCADE, related_name='imagenes3')
    imagen = models.ImageField(upload_to='Imagenes1/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Social_imagen4(models.Model):
    social = models.ForeignKey(Social, on_delete=models.CASCADE, related_name='imagenes4')
    imagen = models.ImageField(upload_to='Imagenes1/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name
    
###################################################################################################

from django.db import models

class Energetico(models.Model):
    imagen_energetico = models.ImageField(upload_to='energetico/', null=True, blank=True)  
    titulo_energetico = models.CharField(max_length=200)
    fecha_energetico = models.DateField()
    servicio = models.CharField(max_length=100)
    nombre_ciudad = models.CharField(max_length=100)
    nombre_tipo_servicio = models.CharField(max_length=100)
    texto_energetico = models.TextField()
    imagen1 = models.ImageField(upload_to='Imagenes2/', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='Imagenes2/', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='Imagenes2/', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='Imagenes2/', null=True, blank=True)

    def __str__(self):
        return self.titulo_energetico

class Energetico_imagen1(models.Model):
    energetico = models.ForeignKey(Energetico, on_delete=models.CASCADE, related_name='imagenes1')
    imagen = models.ImageField(upload_to='Imagenes2/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Energetico_imagen2(models.Model):
    energetico = models.ForeignKey(Energetico, on_delete=models.CASCADE, related_name='imagenes2')
    imagen = models.ImageField(upload_to='Imagenes2/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Energetico_imagen3(models.Model):
    energetico = models.ForeignKey(Energetico, on_delete=models.CASCADE, related_name='imagenes3')
    imagen = models.ImageField(upload_to='Imagenes2/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Energetico_imagen4(models.Model):
    energetico = models.ForeignKey(Energetico, on_delete=models.CASCADE, related_name='imagenes4')
    imagen = models.ImageField(upload_to='Imagenes2/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name
    
    
###################################################################################################

from django.db import models

class Vivienda(models.Model):
    imagen_vivienda = models.ImageField(upload_to='vivienda/', null=True, blank=True)  
    titulo_vivienda = models.CharField(max_length=200)
    fecha_vivienda = models.DateField()
    servicio = models.CharField(max_length=100)
    nombre_ciudad = models.CharField(max_length=100)
    nombre_tipo_servicio = models.CharField(max_length=100)
    texto_vivienda = models.TextField()
    imagen1 = models.ImageField(upload_to='Imagenes3/', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='Imagenes3/', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='Imagenes3/', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='Imagenes3/', null=True, blank=True)

    def __str__(self):
        return self.titulo_vivienda

class Vivienda_imagen1(models.Model):
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE, related_name='imagenes1')
    imagen = models.ImageField(upload_to='Imagenes3/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Vivienda_imagen2(models.Model):
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE, related_name='imagenes2')
    imagen = models.ImageField(upload_to='Imagenes3/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Vivienda_imagen3(models.Model):
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE, related_name='imagenes3')
    imagen = models.ImageField(upload_to='Imagenes3/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Vivienda_imagen4(models.Model):
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE, related_name='imagenes4')
    imagen = models.ImageField(upload_to='Imagenes3/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name
    
    
###################################################################################################

from django.db import models

class Reconstruccion(models.Model):
    imagen_reconstruccion = models.ImageField(upload_to='reconstruccion/', null=True, blank=True)  
    titulo_reconstruccion = models.CharField(max_length=200)
    fecha_reconstruccion = models.DateField()
    servicio = models.CharField(max_length=100)
    nombre_ciudad = models.CharField(max_length=100)
    nombre_tipo_servicio = models.CharField(max_length=100)
    texto_reconstruccion = models.TextField()
    imagen1 = models.ImageField(upload_to='Imagenes4/', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='Imagenes4/', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='Imagenes4/', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='Imagenes4/', null=True, blank=True)

    def __str__(self):
        return self.titulo_reconstruccion

class Reconstruccion_imagen1(models.Model):
    reconstruccion = models.ForeignKey(Reconstruccion, on_delete=models.CASCADE, related_name='imagenes1')
    imagen = models.ImageField(upload_to='Imagenes4/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Reconstruccion_imagen2(models.Model):
    reconstruccion = models.ForeignKey(Reconstruccion, on_delete=models.CASCADE, related_name='imagenes2')
    imagen = models.ImageField(upload_to='Imagenes4/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Reconstruccion_imagen3(models.Model):
    reconstruccion = models.ForeignKey(Reconstruccion, on_delete=models.CASCADE, related_name='imagenes3')
    imagen = models.ImageField(upload_to='Imagenes4/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Reconstruccion_imagen4(models.Model):
    reconstruccion = models.ForeignKey(Reconstruccion, on_delete=models.CASCADE, related_name='imagenes4')
    imagen = models.ImageField(upload_to='Imagenes4/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name
    

###################################################################################################

from django.db import models

class Verdes(models.Model):
    imagen_verdes = models.ImageField(upload_to='verdes/', null=True, blank=True)  
    titulo_verdes = models.CharField(max_length=200)
    fecha_verdes = models.DateField()
    servicio = models.CharField(max_length=100)
    nombre_ciudad = models.CharField(max_length=100)
    nombre_tipo_servicio = models.CharField(max_length=100)
    texto_verdes = models.TextField()
    imagen1 = models.ImageField(upload_to='Imagenes5/', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='Imagenes5/', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='Imagenes5/', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='Imagenes5/', null=True, blank=True)

    def __str__(self):
        return self.titulo_verdes

class Verdes_imagen1(models.Model):
    verdes = models.ForeignKey(Verdes, on_delete=models.CASCADE, related_name='imagenes1')
    imagen = models.ImageField(upload_to='Imagenes5/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Verdes_imagen2(models.Model):
    verdes = models.ForeignKey(Verdes, on_delete=models.CASCADE, related_name='imagenes2')
    imagen = models.ImageField(upload_to='Imagenes5/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Verdes_imagen3(models.Model):
    verdes = models.ForeignKey(Verdes, on_delete=models.CASCADE, related_name='imagenes3')
    imagen = models.ImageField(upload_to='Imagenes5/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Verdes_imagen4(models.Model):
    verdes = models.ForeignKey(Verdes, on_delete=models.CASCADE, related_name='imagenes4')
    imagen = models.ImageField(upload_to='Imagenes5/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

###################################################################################################

from django.db import models

class Condominio(models.Model):
    imagen_condominio = models.ImageField(upload_to='condominio/', null=True, blank=True)  
    titulo_condominio = models.CharField(max_length=200)
    fecha_condominio = models.DateField()
    servicio = models.CharField(max_length=100)
    nombre_ciudad = models.CharField(max_length=100)
    nombre_tipo_servicio = models.CharField(max_length=100)
    texto_condominio = models.TextField()
    imagen1 = models.ImageField(upload_to='Imagenes6/', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='Imagenes6/', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='Imagenes6/', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='Imagenes6/', null=True, blank=True)

    def __str__(self):
        return self.titulo_condominio

class Condominio_imagen1(models.Model):
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='imagenes1')
    imagen = models.ImageField(upload_to='Imagenes6/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Condominio_imagen2(models.Model):
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='imagenes2')
    imagen = models.ImageField(upload_to='Imagenes6/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Condominio_imagen3(models.Model):
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='imagenes3')
    imagen = models.ImageField(upload_to='Imagenes6/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Condominio_imagen4(models.Model):
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='imagenes4')
    imagen = models.ImageField(upload_to='Imagenes6/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name
    
###################################################################################################

from django.db import models

class Asbesto(models.Model):
    imagen_asbesto = models.ImageField(upload_to='asbesto/', null=True, blank=True)  
    titulo_asbesto = models.CharField(max_length=200)
    fecha_asbesto = models.DateField()
    servicio = models.CharField(max_length=100)
    nombre_ciudad = models.CharField(max_length=100)
    nombre_tipo_servicio = models.CharField(max_length=100)
    texto_asbesto = models.TextField()
    imagen1 = models.ImageField(upload_to='Imagenes7/', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='Imagenes7/', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='Imagenes7/', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='Imagenes7/', null=True, blank=True)

    def __str__(self):
        return self.titulo_asbesto

class Asbesto_imagen1(models.Model):
    asbesto = models.ForeignKey(Asbesto, on_delete=models.CASCADE, related_name='imagenes1')
    imagen = models.ImageField(upload_to='Imagenes7/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Asbesto_imagen2(models.Model):
    asbesto = models.ForeignKey(Asbesto, on_delete=models.CASCADE, related_name='imagenes2')
    imagen = models.ImageField(upload_to='Imagenes7/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Asbesto_imagen3(models.Model):
    asbesto = models.ForeignKey(Asbesto, on_delete=models.CASCADE, related_name='imagenes3')
    imagen = models.ImageField(upload_to='Imagenes7/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Asbesto_imagen4(models.Model):
    asbesto = models.ForeignKey(Asbesto, on_delete=models.CASCADE, related_name='imagenes4')
    imagen = models.ImageField(upload_to='Imagenes7/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name
    


###################################################################################################

from django.db import models

class Comunitaria(models.Model):
    imagen_comunitaria = models.ImageField(upload_to='comunitaria/', null=True, blank=True)  
    titulo_comunitaria = models.CharField(max_length=200)
    fecha_comunitaria = models.DateField()
    servicio = models.CharField(max_length=100)
    nombre_ciudad = models.CharField(max_length=100)
    nombre_tipo_servicio = models.CharField(max_length=100)
    texto_comunitaria = models.TextField()
    imagen1 = models.ImageField(upload_to='Imagenes8/', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='Imagenes8/', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='Imagenes8/', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='Imagenes8/', null=True, blank=True)

    def __str__(self):
        return self.titulo_comunitaria

class Comunitaria_imagen1(models.Model):
    comunitaria = models.ForeignKey(Comunitaria, on_delete=models.CASCADE, related_name='imagenes1')
    imagen = models.ImageField(upload_to='Imagenes8/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Comunitaria_imagen2(models.Model):
    comunitaria = models.ForeignKey(Comunitaria, on_delete=models.CASCADE, related_name='imagenes2')
    imagen = models.ImageField(upload_to='Imagenes8/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Comunitaria_imagen3(models.Model):
    comunitaria = models.ForeignKey(Comunitaria, on_delete=models.CASCADE, related_name='imagenes3')
    imagen = models.ImageField(upload_to='Imagenes8/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name

class Comunitaria_imagen4(models.Model):
    comunitaria = models.ForeignKey(Comunitaria, on_delete=models.CASCADE, related_name='imagenes4')
    imagen = models.ImageField(upload_to='Imagenes8/', null=True, blank=True)

    def __str__(self):
        return self.imagen.name
    
###################################################################################################

# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    cargo = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    foto_de_perfil = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    imagen_de_fondo = models.ImageField(upload_to='background_images/', blank=True, null=True)

    def __str__(self):
        return self.username
    
###################################################################################################    


class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username

###################################################################################################

from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)  

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad, related_name='comunas', on_delete=models.CASCADE)

class Ubicacion(models.Model):
    nombre_lugar = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    comuna = models.CharField(max_length=255)
    latitud = models.FloatField()
    longitud = models.FloatField()
    
    