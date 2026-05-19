from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    genre = models.CharField(max_length=100, verbose_name="Género")
    director = models.CharField(max_length=150, verbose_name="Director")
    year = models.IntegerField(verbose_name="Año de publicación")
    synopsis = models.TextField(verbose_name="Sinopsis")
    image = models.ImageField(upload_to='movies/', null=True, blank=True, verbose_name="Imagen")

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"

    def __str__(self):
        return self.title
