from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy



class RegisterUserView(CreateView):
    form_class = UserCreationForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('authorization')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'

        return context
    

class AuthorizationUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/authorization.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context
    
    def get_success_url(self):
        return reverse_lazy('payment_requests')
