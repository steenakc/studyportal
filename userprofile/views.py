from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

class UserLoginView(LoginView):
    template_name = 'registration/login.html'

class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = 'home'

    def get_success_url(self, **kwargs):
        return reverse_lazy('login')

class DashboardView(TemplateView):
    template_name = 'userprofile/dashboard.html'
    
