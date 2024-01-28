from django.urls import path
from ajax import views

urlpatterns = [
    path('', views.get_requisites, name='get_requisites')
]