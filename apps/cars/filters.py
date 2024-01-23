from django.db.models import QuerySet
from django.http import QueryDict

from .models import CarModel


def cars_filter(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()
    for k, v in query.items():
        match k:
            case 'year_lt':
                qs = qs.filter(year__lt=v)
            case 'year__gt':
                qs = qs.filter(year__gt=v)
            case 'year_gte':
                qs = qs.filter(year__gte=v)
            case 'year__lte':
                qs = qs.filter(year__lte=v)
            case 'model__iendswith':
                qs = qs.filter(model__iendswith=v)
            case 'model__icontains':
                qs = qs.filter(model__icontains =v)
            case 'model__istartswith':
                qs = qs.filter(model__istartswith=v)
            case 'sort':
                qs = qs.order_by(v)
            case 'sort_max':
                qs = qs.order_by(f'-{v}')

    return qs
