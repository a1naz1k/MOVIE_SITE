from .models import Movie
from django_filters import FilterSet


class MovieFilter(FilterSet):

    class Meta:
        model = Movie
        fields = {
            'status_movie': ['exact'],
            'genre': ['exact'],
            'country': ['exact'],
            'director': ['exact'],
            'actor': ['exact'],
             'year': ['gt', 'lt'],
        }
