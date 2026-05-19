from django.shortcuts import get_object_or_404, render
from .models import Movie


def index(request):
    """Vista para mostrar el listado de películas"""
    movies = Movie.objects.order_by('title')
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)


def detail(request, pk):
    """Vista para mostrar la ficha de una película"""
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/detail.html', {'movie': movie})


def no_piratees(request):
    """Vista de broma para advertir sobre piratería"""
    return render(request, 'movies/no_piratees.html')
