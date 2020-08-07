from django.db import models

# Create your models here.
ESTADO_DEL_LIBRO = [
    ('IN', 'En biblioteca'),
    ('BW', 'Prestado'),
    ('RQ', 'Pedido'),
    ('RV', 'Reservado'),
]

class MateriaLectura(models.Model):
    codigo = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100)
    anio_publicacion = models.DateField()
    status = models.CharField(max_length=2, choices=ESTADO_DEL_LIBRO, default='En biblioteca')
    foto_portada = models.ImageField(max_length=100, upload_to='fotos_tapa/', default='fotos_tapa/default.png', blank=True)
    resumen = models.FileField(upload_to='resumenes/', max_length=100, blank=True)


