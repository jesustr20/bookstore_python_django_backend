import django_filters
from videos.models import Video

class VideoFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Video
        fields = ['title', 'author', 'published_date']