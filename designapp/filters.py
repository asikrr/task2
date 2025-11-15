import django_filters
from .models import DesignRequest

class DesignRequestFilter(django_filters.FilterSet):
    class Meta:
        model = DesignRequest
        fields = ['status']