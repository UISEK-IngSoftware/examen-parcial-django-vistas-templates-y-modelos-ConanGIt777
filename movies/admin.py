from django.contrib import admin
from django.utils.html import format_html
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'genre', 'year', 'image_preview')
    search_fields = ('title', 'director')
    list_filter = ('year', 'genre')
    ordering = ('-year',)
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'director', 'genre', 'year')
        }),
        ('Contenido', {
            'fields': ('synopsis', 'image')
        }),
    )

    def image_preview(self, obj):
        """Mostrar preview de la imagen en la lista"""
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="75" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return "Sin imagen"
    image_preview.short_description = "Imagen"
