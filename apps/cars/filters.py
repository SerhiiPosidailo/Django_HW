from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from .models import CarModel
from .serializers import CarSerializer



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

            case'order':
                fields = CarSerializer.Meta.fields
                fields = [*fields, *[f'-{field}' for field in fields]]

                if v not in fields:
                    raise ValidationError({'details': f'Please choice order from {", ".join(fields)}'})

                qs = qs.order_by(v)
            case _:
                raise ValidationError({'Details': f'{k} is not a allowed here'})

    return qs
