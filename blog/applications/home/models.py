from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.

class Home(TimeStampedModel):
    """Modelo para datos de la pantalla home"""

    title = models.CharField('Nombre', max_length=50)
    description = models.TextField()
    about_title = models.CharField('Titulo Nosotros', max_length=50)
    about_text =  models.TextField('About text', blank=True, null=True)
    email = models.CharField('Email de contacto', max_length=20,  blank=True, null=True )
    phone = models.CharField('Telefono de contacto', max_length=20,  blank=True, null=True)

    class Meta:
        verbose_name = "Pagina Principal"
        verbose_name_plural = "Pagina Principal"

    def __str__(self):
        return self.title
    

    
class Suscribirse(TimeStampedModel):
    """Modelo suscriptor"""

    email = models.EmailField(max_length=254, unique=True)

    class Meta:
        verbose_name = "Suscriptor"
        verbose_name_plural = "Suscriptores"

    def __str__(self):
        return self.email
    


class Contact(TimeStampedModel):
    """Formulario de Contacto"""

    full_name = models.CharField('Nombres', max_length=60)
    email = models.EmailField(max_length=254, unique=True)
    message = models.TextField()


    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Mensajes"

    def __str__(self):
        return self.full_name
    