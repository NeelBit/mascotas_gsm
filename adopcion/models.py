from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django import forms

from django.contrib.auth.models import User
#from django.conf import settings

from datetime import datetime

"""
Borrar registros automaticamente después de 120, permanecer siempre en 120 registros
"""

class Post(models.Model):
    fecha_publi = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de publicación')
    descripcion = models.TextField(max_length=1000, help_text='Por favor sea lo mayormente descriptivo, hasta 1000 caracteres.', verbose_name='Descripción')
    contacto = models.CharField(max_length=200, help_text='Coloque las formas de contacto, por favor verifique.', verbose_name='Contacto')
    disponibilidad = models.BooleanField(default=True, blank=True, verbose_name='Disponibilidad')
    
    #probando cambiar disponibilidad
    """ @property
    def noDisponible(self):
        self.disponibilidad = False
        return self.disponibilidad """
    
    
    #probando
    #author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #author = models.ForeignKey("auth.User", verbose_name=("author"), on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    ESPECIES = (
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('otro', 'Otro'),
    )
    #default='otro', 
    tipo = models.CharField(choices=ESPECIES, max_length=10, help_text='Seleccione la especie.')
    
    nombre = models.CharField(null=True, blank=True, max_length=20, help_text='Si es que ya tiene nombre. Sino deje en blanco', default='Sin nombre aún :(')
    raza = models.CharField(null=True, blank=True, max_length=20, help_text='Solo escribe si conoces la raza. Sino deje en blanco')
    
    MEDIDAS = (
        ('chico', 'Pequeño'),
        ('mediano', 'Mediano'),
        ('grande', 'Grande'),
        ('otro', 'No se'),
    )
    medida = models.CharField(choices=MEDIDAS, default='otro', max_length=15, help_text='Seleccione el tamaño que cree mas adecuado.')
    
    def user_directory_path(self, filename):
  
        # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
        """ return 'user_{0}/{1}'.format(instance.user.id, filename) """
        
        #return 'user_{0}/% Y/% m/{1}'.format(instance.user.id, filename)

        year = datetime.now().year
        month = datetime.now().month
        return f'user_{self.autor.id}/{year}/{month}/{filename}'
        
        #upload_to ='uploads/% Y/% m/% d/'
    
    img1 = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    img2 = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    img3 = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    
    def __str__(self):
        return self.descripcion
    
    # 
    def get_absolute_url(self):
    #Devuelve la url para acceder a una instancia particular del modelo.
        return reverse('post_detail_view', args=[str(self.id)])
    
    
    class Meta():
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        
        ordering = ['-fecha_publi']

""" class Especie(models.Model):
    
    ESPECIES = (
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('otro', 'Otro'),
    )
    
    tipo = models.CharField(choices=ESPECIES, default='otro', max_length=10, help_text='Seleccione la especie.')
    
    def __str__(self):
        return self.tipo
    
    class Meta():
        verbose_name = "Especie"
        verbose_name_plural = "Especies" """

""" class Mascota(models.Model):
    nombre = models.CharField(null=True, blank=True, max_length=20, help_text='Si es que ya tiene nombre. Sino deje en blanco', default='Sin nombre aún :(')
    raza = models.CharField(null=True, blank=True, max_length=20, help_text='Solo escribe si conoces la raza. Sino deje en blanco')
    
    MEDIDAS = (
        ('chico', 'Pequeño'),
        ('mediano', 'Mediano'),
        ('grande', 'Grande'),
        ('otro', 'No se'),
    )
    
    
    #medida = models.CharField(max_length=20, help_text='Que tamaño tiene?', default='otro') #default='otro', #este funciona
    
    medida = models.CharField(choices=MEDIDAS, default='otro', max_length=15, help_text='Seleccione el tamaño que cree mas adecuado.')
    
    #foto1 = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    #foto2 = 
    #foto3 = 
    
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nombre}, de especie {self.especie.tipo}.'
    
    class Meta():
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas" """