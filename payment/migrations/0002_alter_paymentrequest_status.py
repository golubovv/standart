# Generated by Django 5.0.1 on 2024-01-27 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentrequest',
            name='status',
            field=models.CharField(choices=[('waiting', 'waiting'), ('paid', 'paid'), ('canceled', 'canceled')], default='waiting', max_length=50),
        ),
    ]