from django.db.models.query import QuerySet
from django.views.generic import ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.response import Response

from .models import PaymentRequest, Requisites
from .forms import SortRequisitesForm
from .serializers import CreatePaymentRequestSerializer, RetrievePaymentRequestSerializer


class PaymentRequestsList(ListView):
    model = PaymentRequest
    context_object_name = 'payment_requests'
    template_name = 'payment/payment_requests.html'

    def get_queryset(self):
        return PaymentRequest.objects.all().select_related('requisites')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заявки на оплату'
        return context


class RequisitesList(LoginRequiredMixin, ListView, FormView):
    model = Requisites
    context_object_name = 'requisites_list'
    template_name = 'payment/requisites.html'
    form_class = SortRequisitesForm
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список реквизитов'
        return context
    

class CreatePaymentRequestAPIView(generics.CreateAPIView):
    serializer_class = CreatePaymentRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        instance = serializer.save()
        return Response({
            'id': instance.pk,
            'full_name': instance.requisites.full_name,
            'phone_number': instance.requisites.phone_number,
            'tender_type': instance.requisites.tender_type,
            'payment_limit': instance.requisites.payment_limit
        })


class GetPaymentRequestStatusAPIView(generics.RetrieveAPIView):
    queryset = PaymentRequest.objects.all()
    serializer_class = RetrievePaymentRequestSerializer