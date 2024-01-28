from django.db import models

payment_statuses = {
    'waiting': 'waiting',
    'paid': 'paid',
    'canceled': 'canceled'
}

class PaymentRequest(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(max_length=50, choices=payment_statuses, default='waiting')
    requisites = models.ForeignKey('Requisites', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.requisites.full_name}, {self.amount}'
    

card_types = {
    'debit_card': 'debit_card',
    'credit_card': 'credit_card',
    'prepaid_card': 'prepaid_card',
    'overdraft_card': 'overdraft_card'
}
account_types = {
    'current_account': 'current_account',
    'credit_account': 'credit_account',
    'currency_account': 'currency_account',
    'deposit_account': 'deposit_account'
}

class Requisites(models.Model):
    tender_type = models.CharField(max_length=50, choices=card_types|account_types)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    payment_limit = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.full_name}, {self.tender_type}'
