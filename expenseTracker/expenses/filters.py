from .model import Expense
from django_filters import rest_framework as filters

class ExpenseFilter(filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')
    # manufacturer__name = django_filters.CharFilter(lookup_expr='icontains')

    category = filters.NumberFilter(field_name='category__id')
    created_at__gt = filters.NumberFilter(field_name='created_at', lookup_expr='gt')
    created_at__lt = filters.NumberFilter(field_name='created_at', lookup_expr='lt')

    # release_year = django_filters.NumberFilter(field_name='release_date', lookup_expr='year')
    # release_year__gt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__gt')
    # release_year__lt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__lt')

    class Meta:
        model = Expense
        fields = ['category', 'created_at']