import django_filters
from .models import Staff


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Staff
        fields = ['category']
