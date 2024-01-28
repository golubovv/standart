from django.core.management.base import BaseCommand

from random import choice, randint

from ...models import PaymentRequest, Requisites, card_types, account_types, payment_statuses

names = [
    'Кирилл', 'Виктор', 'Алан', 'Александр',
    'Дмитрий', 'Владислав', 'Пётр', 'Максим',
    'Иван', 'Никита', 'Владимир', 'Ильшат'
]
surnames = [
    'Баженов', 'Коновалов', 'Скворцов',
    'Орлов', 'Гилязов', 'Калюка',
    'Бесоногов', 'Мартюшев', 'Кетов'
]
middle_names = [
    'Сергеевич', 'Александрович', 
    'Викторович', 'Петрович',
    'Иванович', 'Владиславович'
]
numbers = [str(i) for i in range(1, 10)]

class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми значениями'

    def handle(self, *args, **options):
        PaymentRequest.objects.all().delete()
        Requisites.objects.all().delete()

        for _ in range(100):
            Requisites.objects.create(
                tender_type=choice(list(card_types.values())+list(account_types.values())),
                full_name=f'{choice(surnames)} {choice(names)} {choice(middle_names)}',
                phone_number=f'+7{"".join([choice(numbers) for i in range(9)])}',
                payment_limit=choice([200000, 1000000, 300000])
            )
        
        for _ in range(5000):
            PaymentRequest.objects.create(
                amount=randint(100, 100000),
                status=choice(list(payment_statuses.values())),
                requisites=choice(Requisites.objects.all())
            )