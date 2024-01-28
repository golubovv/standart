from django import forms

choice_fields = {
    'full_name': 'ФИО',
    'phone_number': 'Номер телефона',
    'tender_type': 'Тип платёжного средства',
    'payment_limit': 'Лимит платежа'
}

class SortRequisitesForm(forms.Form):
    order_by = forms.ChoiceField(choices=choice_fields, label='Сортировка по полю:')
    search_field = forms.ChoiceField(choices=choice_fields, label='Поиск в поле:')
    search_by = forms.CharField(max_length=100, label='По содержимому:')