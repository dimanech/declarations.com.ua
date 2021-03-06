from django_jinja import library
from decimal import Decimal
from django.utils.safestring import mark_safe


@library.global_function
def updated_querystring(request, params):
    """Updates current querystring with a given dict of params, removing
    existing occurrences of such params. Returns a urlencoded querystring."""
    original_params = request.GET.copy()
    for key in params:
        if key in original_params:
            original_params.pop(key)
    original_params.update(params)
    return original_params.urlencode()


@library.filter
def curformat(value):
    if value and value != "0":
        return '{:,.2f}'.format(
            float(value.replace(',', '.'))).replace(',', ' ').replace('.', ',')
    else:
        return mark_safe('<i class="currency-empty">–</i>')
