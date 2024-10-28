import django_filters
from documentals.models import Documental

class DocumentalFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Documental
        fields = ['title', 'author', 'published_date']