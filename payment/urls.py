from django.urls import path

from payment import views

urlpatterns = [
    path('',
          views.PaymentRequestsList.as_view(), name='payment_requests'),
    path('requisites',
          views.RequisitesList.as_view(), name='requisites'),
    path('api/v1/create_invoice',
         views.CreatePaymentRequestAPIView.as_view(), name='create_invoice'),
    path('api/v1/get_invoice_status/<int:pk>', 
         views.GetPaymentRequestStatusAPIView.as_view(), name='get_invoice_status')
]