import django_filters
from django.contrib.auth.models import User

class UserFilter(django_filters.FilterSet):
    # firstname = django_filters.CharFilter(lookup_expr='icontains')
    # username = django_filters.CharFilter(lookup_expr='icontains')
    # email = django_filters.CharFilter(lookup_expr='icontains')
    

    class Meta:
        model = User
        fields = {
            'id': ['exact'],
            'is_active': ['exact'],
            'first_name': ['icontains'],
            'email': ['exact']
        }
