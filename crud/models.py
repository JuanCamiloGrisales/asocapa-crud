from django.db import models

# Create your models here.
class Cliente(models.Model):
    '''Model definition for ModelName.'''
    nombre = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    residencia = models.CharField(max_length=200)
    megas = models.CharField(max_length=200)


    class Meta:
        '''Meta definition for ModelName.'''

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombre