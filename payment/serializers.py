from rest_framework import serializers

from .models import PaymentRequest


class CreatePaymentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentRequest
        fields = ('requisites', 'amount')
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'full_name': instance.requisites.full_name,
            'phone_number': instance.requisites.phone_number,
            'tender_type': instance.requisites.tender_type,
            'payment_limit': instance.requisites.payment_limit,
        }


class RetrievePaymentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentRequest
        fields = ('id')
    
    def to_representation(self, instance):
        return {
            'status': instance.status
        }