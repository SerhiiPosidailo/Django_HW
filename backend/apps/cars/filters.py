from django_filters import rest_framework as filters


class CarFilter(filters.FilterSet):
    year_lt = filters.NumberFilter('year', 'lt')
    year_gt = filters.NumberFilter('year', 'gt')
    model = filters.CharFilter('model', 'icontains')
    order = filters.OrderingFilter(
        fields=(
            'id',
            'model',
            'year',
            'body_type',
            'engine_capacity'
        )
    )
