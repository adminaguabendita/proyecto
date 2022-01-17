from django.db import models

# Create your models here.



# Create your models here.
class Tienda(models.Model):
    co = models.CharField(primary_key=True, max_length=3)
    descripcion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Tienda'
        verbose_name_plural = 'Tiendas'
        db_table = 'Tienda'
