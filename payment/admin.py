from django.contrib import admin

from .models import PaymentRequest, Requisites


class RequisitesAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'tender_type', 'phone_number')
    list_display_links = ('full_name',)
    search_fields = ('full_name', 'tender_type', 'phone_number')


class PaymentRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'status', 'requisites')
    list_display_links = ('id', 'amount', 'status', 'requisites')
    search_fields = ('id', 'amount', 'status')


admin.site.register(PaymentRequest, PaymentRequestAdmin)
admin.site.register(Requisites, RequisitesAdmin)
