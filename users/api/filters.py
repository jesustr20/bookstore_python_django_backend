import django_filters
from users.models import User

class UserFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = User
        fields = ['email','first_name','last_name','is_active',
                  'is_staff','articles','books','documentals',
                  'videos','comments'
                ]