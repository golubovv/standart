from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

from user import views

urlpatterns = [
    path('register', 
         views.RegisterUserView.as_view(), name='registration'),
    path('login', 
         views.AuthorizationUserView.as_view(), name='authorization'),
    path('logout', 
         LogoutView.as_view(), name='logout'),
]