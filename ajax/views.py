from django.http import JsonResponse

from payment.models import Requisites


def get_requisites(request):
    fields = [field.name for field in Requisites._meta.fields]
    search_field = request.GET.get('search_field')
    search_by = request.GET.get('search_by')
    if search_field in fields and search_by != 'None':
        filter_kwargs = {
            f"{search_field}__icontains": search_by
        }
        requisites = Requisites.objects.filter(**filter_kwargs)
    else: 
        requisites = Requisites.objects.all()

    sort_field = request.GET.get('order_by')
    if sort_field in fields:
        requisites = requisites.order_by(sort_field)
    else:
        requisites = requisites

    return JsonResponse(list(requisites.values()), safe=False)
